from __future__ import annotations
from pathlib import Path
import nbformat as nbf

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK_PATH = ROOT / 'notebooks' / '005_empirical_bayes_examples_gifs.ipynb'
NOTEBOOK_PATH.parent.mkdir(parents=True, exist_ok=True)

nb = nbf.v4.new_notebook()
nb.metadata = {
    'kernelspec': {'display_name':'Python (dev_statistics venv)','language':'python','name':'dev_statistics_venv'},
    'language_info': {'name':'python','version':'3.11'},
}

cells=[]

cells.append(nbf.v4.new_markdown_cell(r'''# 経験ベイズ（Empirical Bayes）の事例を4つGIFで理解する

経験ベイズは、階層モデルの上位分布（事前分布・母集団分布）のパラメータを、外から固定するのではなく **データ全体から推定** してから、各グループの推定に使う考え方です。

```text
全グループのデータから prior / hyperparameter を推定
        ↓
その推定 prior を使って各グループの posterior を計算
        ↓
小標本・ノイズの大きいグループほど全体平均へ縮む
```

このノートでは、保存済みローカル公開データだけを使って、次の4つを可視化します。

1. **Beta-Binomial EB**: グループ別の比率を、全体から推定した Beta prior で平滑化する。
2. **Gamma-Poisson EB**: グループ別のカウント率を、全体から推定した Gamma prior で平滑化する。
3. **Normal-Normal EB**: グループ別の平均を、全体から推定した Normal prior で縮約する。
4. **EBランキング補正**: 小標本グループが上位/下位に出すぎる問題を、EB推定で補正する。
'''))

cells.append(nbf.v4.new_code_cell(r'''# 1. Imports / paths / theme
from __future__ import annotations

import warnings
from pathlib import Path

import imageio.v2 as imageio
import japanize_matplotlib
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy.optimize import minimize
from scipy.special import betaln, expit, gammaln, logit
from scipy.stats import beta as beta_dist, gamma as gamma_dist, norm

warnings.filterwarnings('ignore', category=RuntimeWarning)
warnings.filterwarnings('ignore', category=UserWarning)

sns.set_theme(style='whitegrid', palette='muted', font_scale=1.0)
japanize_matplotlib.japanize()
plt.rcParams['figure.dpi'] = 110
plt.rcParams['savefig.dpi'] = 130
plt.rcParams['axes.unicode_minus'] = False

PROJECT_ROOT = Path.cwd()
if PROJECT_ROOT.name == 'notebooks':
    PROJECT_ROOT = PROJECT_ROOT.parent
DATA_DIR = PROJECT_ROOT / 'data' / 'raw'
GIF_DIR = PROJECT_ROOT / 'outputs' / 'gifs'
FIG_DIR = PROJECT_ROOT / 'outputs' / 'figures'
for p in [DATA_DIR, GIF_DIR, FIG_DIR]:
    p.mkdir(parents=True, exist_ok=True)
RNG = np.random.default_rng(20260620)
print(f'PROJECT_ROOT = {PROJECT_ROOT}')
print(f'DATA_DIR     = {DATA_DIR}')
'''))

cells.append(nbf.v4.new_code_cell(r'''# 2. Load locally saved public data
DATA_FILES = {
    'tips': DATA_DIR / 'tips.csv',
    'penguins': DATA_DIR / 'penguins.csv',
    'mpg': DATA_DIR / 'mpg.csv',
}

def load_local_csv(name: str) -> pd.DataFrame:
    path = DATA_FILES[name]
    if not path.exists():
        raise FileNotFoundError(f'{path} が見つかりません。data/raw/ に公開データを保存してください。')
    print(f'{name:<8} <- {path.relative_to(PROJECT_ROOT).as_posix()}')
    return pd.read_csv(path)

tips = load_local_csv('tips')
penguins = load_local_csv('penguins')
mpg = load_local_csv('mpg')
print('tips    ', tips.shape)
print('penguins', penguins.shape)
print('mpg     ', mpg.shape)
'''))

cells.append(nbf.v4.new_code_cell(r'''# 3. Shared helpers
def fig_to_frame(fig):
    fig.canvas.draw()
    rgba = np.asarray(fig.canvas.buffer_rgba())
    return rgba[:, :, :3].copy()

def save_gif(frames, path: Path, fps: int = 9) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    imageio.mimsave(path, frames, duration=1 / fps, loop=0)
    print(f'saved {path} ({len(frames)} frames, {fps} fps)')
    return path

def add_note(ax, text: str, loc=(0.02, 0.98), fontsize=9):
    ax.text(loc[0], loc[1], text, transform=ax.transAxes, va='top', ha='left', fontsize=fontsize,
            bbox={'boxstyle':'round,pad=0.35','fc':'white','ec':'0.75','alpha':0.93})

def smooth_path(start, end, n=56):
    s = np.linspace(0, 1, n)
    s = s * s * (3 - 2 * s)
    return [(1 - si) * np.asarray(start, float) + si * np.asarray(end, float) for si in s]

def linear_path(start, end, n=46):
    s = np.linspace(0, 1, n)
    return [(1 - si) * np.asarray(start, float) + si * np.asarray(end, float) for si in s]
'''))

cells.append(nbf.v4.new_markdown_cell(r'''## 1. Beta-Binomial EB: 小標本の比率を平滑化する

`tips.csv` の `day × time` ごとの喫煙率を例にします。

- 観測モデル: $y_j \sim \mathrm{Binomial}(n_j, p_j)$
- EB prior: $p_j \sim \mathrm{Beta}(\alpha,\beta)$
- データ全体から $m,\kappa$ を推定し、$\alpha=m\kappa,\beta=(1-m)\kappa$ とする。

観測比率 $y_j/n_j$ は小さいグループほど極端になりやすい。EB推定では、全体から学んだ prior によって小標本グループほど強く縮みます。
'''))

cells.append(nbf.v4.new_code_cell(r'''def beta_binomial_agg():
    df = tips[['day','time','smoker']].dropna().copy()
    df['is_smoker'] = (df['smoker'].astype(str) == 'Yes').astype(int)
    df['group'] = df['day'].astype(str) + '-' + df['time'].astype(str)
    agg = df.groupby('group')['is_smoker'].agg(y='sum', n='count').reset_index()
    agg = agg[agg['n'] >= 5].sort_values('group').reset_index(drop=True)
    agg['raw'] = agg['y'] / agg['n']
    return agg

def bb_nll(params, y, n):
    m = expit(params[0]); k = np.exp(params[1])
    a = max(m*k, 1e-8); b = max((1-m)*k, 1e-8)
    return float(-np.sum(betaln(y+a, n-y+b) - betaln(a,b)))

def fit_bb(agg):
    y=agg['y'].to_numpy(float); n=agg['n'].to_numpy(float)
    m0=np.clip(y.sum()/n.sum(), .02, .98)
    res=minimize(bb_nll, [logit(m0), np.log(8.0)], args=(y,n), method='Nelder-Mead')
    return float(expit(res.x[0])), float(np.exp(res.x[1]))

def make_eb_beta_binomial_gif():
    agg=beta_binomial_agg(); y=agg['y'].to_numpy(float); n=agg['n'].to_numpy(float)
    m_hat,k_hat=fit_bb(agg)
    # frame 0: weak/non-informative; final: EB prior learned from all groups
    states=linear_path([0.5, 0.15], [m_hat, k_hat], 46)
    x=np.arange(len(agg)); labels=agg['group'].tolist(); grid=np.linspace(.001,.999,400)
    frames=[]; widths=[]
    for t,(m,k) in enumerate(states):
        a=m*k; b=(1-m)*k
        pa=a+y; pb=b+n-y
        post=pa/(pa+pb); lo=beta_dist.ppf(.05,pa,pb); hi=beta_dist.ppf(.95,pa,pb)
        widths.append(float(np.mean(hi-lo)))
        fig,axs=plt.subplots(1,2,figsize=(12,5.1),constrained_layout=True,gridspec_kw={'width_ratios':[1,1.35]})
        pdf=beta_dist.pdf(grid,a,b)
        axs[0].plot(grid,pdf,lw=2.8,color='#4C72B0')
        axs[0].axvline(m,color='#C44E52',ls='--',lw=1.8)
        axs[0].set_title('EBで推定した prior: p_j ~ Beta(α,β)')
        axs[0].set_xlabel('グループ喫煙率 p_j'); axs[0].set_ylabel('density'); axs[0].set_xlim(0,1)
        axs[0].set_ylim(0,max(8,float(np.nanmax(pdf))*1.1))
        add_note(axs[0],f'step {t}/{len(states)-1}\nα={a:.2f}, β={b:.2f}\nm={m:.2f}, κ={k:.2f}', loc=(0.03,0.80), fontsize=8)
        axs[1].scatter(x,agg['raw'],s=80,color='0.35',label='観測比率 y/n')
        axs[1].vlines(x,lo,hi,color='#DD8452',lw=5,alpha=.45,label='EB posterior 90%')
        axs[1].scatter(x,post,s=95,color='#C44E52',edgecolor='white',zorder=4,label='EB posterior mean')
        axs[1].axhline(m,color='#4C72B0',ls='--',label='prior mean m')
        axs[1].set_xticks(x,labels,rotation=25,ha='right'); axs[1].set_ylim(-.05,1.05)
        axs[1].set_title('小標本グループほど全体平均へ縮む')
        axs[1].set_ylabel('smoker rate'); axs[1].legend(loc='upper right',fontsize=8)
        add_note(axs[1],f'平均90%幅={widths[-1]:.2f}\n黒点→赤点がshrinkage', loc=(0.03,0.38), fontsize=8)
        frames.append(fig_to_frame(fig)); plt.close(fig)
    print(f'EB beta-binomial: m={m_hat:.3f}, kappa={k_hat:.2f}, width first={widths[0]:.3f}, last={widths[-1]:.3f}')
    return save_gif(frames, GIF_DIR/'15_eb_beta_binomial_rates.gif')

gif_15=make_eb_beta_binomial_gif(); gif_15
'''))

cells.append(nbf.v4.new_markdown_cell(r'''## 2. Gamma-Poisson EB: 発生率・平均カウントを平滑化する

`tips.csv` の `day × time` ごとの平均人数を例にします。

- 観測モデル: $Y_j \sim \mathrm{Poisson}(E_j\lambda_j)$
- EB prior: $\lambda_j \sim \mathrm{Gamma}(a,b)$
- $E_j$ はそのグループのテーブル数、$\lambda_j$ は1テーブルあたり平均人数。

全体から Gamma prior を推定し、グループ別 rate を posterior mean に縮約します。
'''))

cells.append(nbf.v4.new_code_cell(r'''def gp_agg():
    df=tips[['day','time','size']].dropna().copy()
    df['group']=df['day'].astype(str)+'-'+df['time'].astype(str)
    agg=df.groupby('group')['size'].agg(y='sum', e='count', raw='mean').reset_index()
    agg=agg[agg['e']>=5].sort_values('group').reset_index(drop=True)
    return agg

def gp_nll(params,y,e):
    m=np.exp(params[0]); k=np.exp(params[1]); a=max(m*k,1e-8); b=max(k,1e-8)
    ll=np.sum(gammaln(y+a)-gammaln(a)-gammaln(y+1)+a*np.log(b)+y*np.log(e)-(y+a)*np.log(b+e))
    return float(-ll)

def fit_gp(agg):
    y=agg['y'].to_numpy(float); e=agg['e'].to_numpy(float); m0=y.sum()/e.sum()
    res=minimize(gp_nll,[np.log(m0),np.log(10.)],args=(y,e),method='Nelder-Mead')
    return float(np.exp(res.x[0])), float(np.exp(res.x[1]))

def make_eb_gamma_poisson_gif():
    agg=gp_agg(); y=agg['y'].to_numpy(float); e=agg['e'].to_numpy(float)
    m_hat,k_raw=fit_gp(agg); k_hat=min(k_raw,18.0) # homogeneous data: cap for readable EB prior
    states=linear_path([float(agg['raw'].mean()*0.75), .30], [m_hat, k_hat], 46)
    x=np.arange(len(agg)); labels=agg['group'].tolist(); grid=np.linspace(.01,max(8,agg['raw'].max()+2),400)
    frames=[]; widths=[]
    for t,(m,k) in enumerate(states):
        a=m*k; b=k; pa=a+y; pb=b+e
        post=pa/pb; lo=gamma_dist.ppf(.05,a=pa,scale=1/pb); hi=gamma_dist.ppf(.95,a=pa,scale=1/pb)
        widths.append(float(np.mean(hi-lo)))
        fig,axs=plt.subplots(1,2,figsize=(12,5.1),constrained_layout=True,gridspec_kw={'width_ratios':[1,1.35]})
        pdf=gamma_dist.pdf(grid,a=a,scale=1/b)
        axs[0].plot(grid,pdf,lw=2.8,color='#4C72B0'); axs[0].axvline(m,color='#C44E52',ls='--')
        axs[0].set_title('EBで推定した prior: λ_j ~ Gamma(a,b)')
        axs[0].set_xlabel('平均人数 λ_j'); axs[0].set_ylabel('density'); axs[0].set_xlim(grid.min(),grid.max())
        axs[0].set_ylim(0,max(2,float(np.nanmax(pdf))*1.1))
        add_note(axs[0],f'step {t}/{len(states)-1}\na={a:.2f}, b={b:.2f}\nmean={m:.2f}\nκ(raw)={k_raw:.1f}', loc=(0.03,0.80), fontsize=8)
        axs[1].scatter(x,agg['raw'],s=80,color='0.35',label='観測平均 y/E')
        axs[1].vlines(x,lo,hi,color='#55A868',lw=5,alpha=.45,label='EB posterior 90%')
        axs[1].scatter(x,post,s=95,color='#2C7F4F',edgecolor='white',zorder=4,label='EB posterior mean')
        axs[1].axhline(m,color='#4C72B0',ls='--',label='prior mean')
        axs[1].set_xticks(x,labels,rotation=25,ha='right'); axs[1].set_ylim(0,max(8,agg['raw'].max()+2))
        axs[1].set_title('Poisson rate の経験ベイズ平滑化')
        axs[1].set_ylabel('mean party size'); axs[1].legend(loc='upper right',fontsize=8)
        add_note(axs[1],f'平均90%幅={widths[-1]:.2f}\nrateを全体へ縮約', loc=(0.03,0.38), fontsize=8)
        frames.append(fig_to_frame(fig)); plt.close(fig)
    print(f'EB gamma-poisson: m={m_hat:.3f}, kappa_raw={k_raw:.2f}, kappa_visualized={k_hat:.2f}, width first={widths[0]:.3f}, last={widths[-1]:.3f}')
    return save_gif(frames, GIF_DIR/'16_eb_gamma_poisson_rates.gif')

gif_16=make_eb_gamma_poisson_gif(); gif_16
'''))

cells.append(nbf.v4.new_markdown_cell(r'''## 3. Normal-Normal EB: グループ平均をデータから推定した prior へ縮約する

`penguins.csv` の `species × sex` ごとの体重平均を例にします。

- 観測近似: $\bar y_j \sim \mathcal{N}(\mu_j, s_j^2)$
- EB prior: $\mu_j \sim \mathcal{N}(\mu_0, \tau^2)$
- $\mu_0,\tau$ はグループ平均のばらつきから推定。

小さい $s_j$ のグループは観測平均を信じ、大きい $s_j$ のグループは prior 平均へ強く縮みます。
'''))

cells.append(nbf.v4.new_code_cell(r'''def nn_penguin_agg():
    df=penguins[['species','sex','body_mass_g']].dropna().copy()
    df['sex']=df['sex'].astype(str).str.upper(); df=df[df['sex'].isin(['MALE','FEMALE'])]
    df['group']=df['species'].astype(str)+'-'+df['sex'].astype(str)
    agg=df.groupby('group')['body_mass_g'].agg(mean='mean',n='count',sd='std').reset_index().sort_values('group').reset_index(drop=True)
    agg=agg[agg['n']>=5].reset_index(drop=True)
    return df,agg

def make_eb_normal_normal_gif():
    df,agg=nn_penguin_agg(); means=agg['mean'].to_numpy(float); n=agg['n'].to_numpy(float)
    sigma=float(df.groupby('group')['body_mass_g'].std().mean()); se=sigma/np.sqrt(n)
    mu0=float(np.average(means,weights=1/np.maximum(se**2,1e-9)))
    tau_hat=float(np.sqrt(max(np.var(means,ddof=1)-np.mean(se**2),1.0)))
    # Equal tau spacing creates many nearly identical late frames.  Resample tau
    # by equal displacement of posterior means so Chinstrap/Gentoo/etc. keep moving.
    tau_candidates=np.geomspace(1.0,tau_hat,700)
    def posterior_mean_for_tau(tau):
        prior_prec=1/tau**2; data_prec=1/se**2
        pv=1/(prior_prec+data_prec)
        return pv*(prior_prec*mu0+data_prec*means)
    candidate_means=np.vstack([posterior_mean_for_tau(float(tau)) for tau in tau_candidates])
    displacement=np.r_[0.0,np.cumsum(np.linalg.norm(np.diff(candidate_means,axis=0),axis=1))]
    if displacement[-1] > 0:
        tau_states=np.interp(np.linspace(0,displacement[-1],46),displacement,tau_candidates)
    else:
        tau_states=np.linspace(1.0,tau_hat,46)
    groups=agg['group'].tolist(); x=np.arange(len(groups)); palette=sns.color_palette('Set2',n_colors=len(groups))
    grid=np.linspace(df['body_mass_g'].min()-500,df['body_mass_g'].max()+500,500)
    frames=[]; widths=[]
    for t,tau in enumerate(tau_states):
        prior_prec=1/tau**2; data_prec=1/se**2
        pv=1/(prior_prec+data_prec); pm=pv*(prior_prec*mu0+data_prec*means); ps=np.sqrt(pv)
        lo=pm-1.64*ps; hi=pm+1.64*ps; widths.append(float(np.mean(hi-lo)))
        fig,axs=plt.subplots(1,2,figsize=(12.2,5.2),constrained_layout=True,gridspec_kw={'width_ratios':[1,1.45]})
        pdf=norm.pdf(grid,mu0,tau)
        axs[0].plot(grid,pdf,lw=2.8,color='#4C72B0'); axs[0].axvline(mu0,color='#C44E52',ls='--')
        axs[0].set_title('EBで推定した prior: μ_j ~ Normal(μ0,τ²)')
        axs[0].set_xlabel('グループ平均 μ_j'); axs[0].set_ylabel('density'); axs[0].set_xlim(grid.min(),grid.max())
        axs[0].set_ylim(0,max(.004,float(np.nanmax(pdf))*1.12))
        add_note(axs[0],f'step {t}/{len(tau_states)-1}\nμ0={mu0:,.0f}g\nτ={tau:,.0f}g\nτ_EB={tau_hat:,.0f}g', loc=(0.03,0.80), fontsize=8)
        for j,g in enumerate(groups):
            vals=df.loc[df['group']==g,'body_mass_g'].to_numpy(float)
            axs[1].scatter(RNG.normal(j,.045,len(vals)), vals, s=17, alpha=.20, color=palette[j], edgecolor='none')
            axs[1].plot([j-.25,j+.25],[means[j],means[j]],color=palette[j],lw=1.4,ls=':',label='観測群平均' if j==0 else None)
            axs[1].vlines(j,lo[j],hi[j],color='#C44E52',lw=4,alpha=.48)
            axs[1].scatter(j,pm[j],s=88,color='#C44E52',edgecolor='white',zorder=4,label='EB posterior mean' if j==0 else None)
        axs[1].axhline(mu0,color='0.25',ls='--',label='EB prior mean μ0')
        axs[1].set_xticks(x,groups,rotation=24,ha='right'); axs[1].set_ylim(df['body_mass_g'].min()-350,df['body_mass_g'].max()+350)
        axs[1].set_title('グループ平均の経験ベイズ縮約')
        axs[1].set_ylabel('body_mass_g'); axs[1].legend(loc='upper right',fontsize=8)
        add_note(axs[1],f'平均90%幅={widths[-1]:.1f}g\n観測平均→EB平均', loc=(0.03,0.38), fontsize=8)
        frames.append(fig_to_frame(fig)); plt.close(fig)
    print(f'EB normal-normal: mu0={mu0:.1f}, tau={tau_hat:.1f}, sigma={sigma:.1f}, width first={widths[0]:.2f}, last={widths[-1]:.2f}')
    return save_gif(frames, GIF_DIR/'17_eb_normal_normal_means.gif')

gif_17=make_eb_normal_normal_gif(); gif_17
'''))

cells.append(nbf.v4.new_markdown_cell(r'''## 4. EBランキング補正: 小標本の極端な順位を補正する

`mpg.csv` の `model_year × origin` ごとの平均 `mpg` をランキングします。

生の平均ランキングでは、サンプル数が少ないグループが偶然上位/下位に出やすくなります。経験ベイズでは、

$$
\hat\mu_j^{EB} = (1-w_j)\mu_0 + w_j\bar y_j
$$

として、標準誤差が大きいグループほど全体平均 $\mu_0$ へ縮めます。
'''))

cells.append(nbf.v4.new_code_cell(r'''def mpg_rank_agg():
    df=mpg[['mpg','model_year','origin']].dropna().copy()
    df['group']='Y'+df['model_year'].astype(int).astype(str)+'-'+df['origin'].astype(str)
    agg=df.groupby('group')['mpg'].agg(mean='mean',n='count',sd='std').reset_index()
    agg=agg[agg['n']>=3].reset_index(drop=True)
    agg['sd']=agg['sd'].fillna(df['mpg'].std())
    return df,agg

def make_eb_ranking_gif():
    df,agg=mpg_rank_agg(); means=agg['mean'].to_numpy(float); n=agg['n'].to_numpy(float)
    sigma=float(df['mpg'].std()); se=sigma/np.sqrt(n)
    mu0=float(np.average(means,weights=n))
    tau=float(np.sqrt(max(np.var(means,ddof=1)-np.mean(se**2),1.0)))
    # animate shrinkage multiplier from raw ranking to EB ranking
    prior_prec=1/tau**2; data_prec=1/se**2
    w=data_prec/(data_prec+prior_prec)
    eb=(1-w)*mu0+w*means
    states=linear_path(means, eb, 46)
    frames=[]; widths=[]
    # choose groups that are most moved plus top/bottom raw to keep readable
    moved=np.abs(eb-means)
    show_idx=np.unique(np.r_[np.argsort(means)[:5], np.argsort(means)[-5:], np.argsort(moved)[-8:]])
    show_idx=show_idx[np.argsort(means[show_idx])]
    labels=agg.loc[show_idx,'group'].tolist(); x=np.arange(len(show_idx))
    for t,cur in enumerate(states):
        cur_show=cur[show_idx]; raw_show=means[show_idx]; eb_show=eb[show_idx]
        post_sd=np.sqrt(1/(data_prec+prior_prec)); lo=cur-1.64*post_sd; hi=cur+1.64*post_sd
        widths.append(float(np.mean((hi-lo)[show_idx])))
        fig,axs=plt.subplots(1,2,figsize=(12.4,5.2),constrained_layout=True,gridspec_kw={'width_ratios':[1.1,1.25]})
        axs[0].scatter(n,means,color='0.45',alpha=.65,label='raw group mean')
        axs[0].scatter(n,cur,color='#C44E52',alpha=.8,label='current EB estimate')
        for i in range(len(agg)):
            if moved[i] > np.quantile(moved,.75):
                axs[0].plot([n[i],n[i]],[means[i],cur[i]],color='#C44E52',alpha=.18)
        axs[0].axhline(mu0,color='#4C72B0',ls='--',label='μ0')
        axs[0].set_xscale('log'); axs[0].set_xlabel('group sample size n_j (log)'); axs[0].set_ylabel('mpg')
        axs[0].set_title('小標本ほどEBで大きく縮む')
        add_note(axs[0],f'step {t}/{len(states)-1}\nμ0={mu0:.1f}\nτ_EB={tau:.1f}\n平均shrink={np.mean(1-w):.2f}', loc=(0.03,0.38), fontsize=8)
        axs[0].legend(loc='upper right', fontsize=8)
        axs[1].hlines(x,raw_show,cur_show,color='0.75',lw=2)
        axs[1].scatter(raw_show,x,color='0.35',s=70,label='raw mean')
        axs[1].errorbar(cur_show,x,xerr=[cur_show-lo[show_idx],hi[show_idx]-cur_show],fmt='o',color='#C44E52',ecolor='#DD8452',elinewidth=3,capsize=0,label='current EB + 90%')
        axs[1].axvline(mu0,color='#4C72B0',ls='--',label='μ0')
        axs[1].set_yticks(x,labels); axs[1].set_xlabel('mpg'); axs[1].set_title('ランキング候補の補正')
        axs[1].legend(fontsize=8,loc='upper right')
        add_note(axs[1],f'平均90%幅={widths[-1]:.1f}\nraw順位を補正', loc=(0.03,0.18), fontsize=8)
        frames.append(fig_to_frame(fig)); plt.close(fig)
    print(f'EB ranking: groups={len(agg)}, mu0={mu0:.2f}, tau={tau:.2f}, width first={widths[0]:.2f}, last={widths[-1]:.2f}')
    return save_gif(frames, GIF_DIR/'18_eb_ranking_correction.gif')

gif_18=make_eb_ranking_gif(); gif_18
'''))

cells.append(nbf.v4.new_markdown_cell(r'''## 5. 作成したGIF

4本とも、観測データは固定し、経験ベイズ推定が「生のグループ推定」から「全体から学んだ prior を使った推定」へ移る様子を表します。
'''))

cells.append(nbf.v4.new_code_cell(r'''from IPython.display import HTML, display
items=[
    ('1. Beta-Binomial EB: 比率の平滑化', gif_15),
    ('2. Gamma-Poisson EB: rateの平滑化', gif_16),
    ('3. Normal-Normal EB: 平均の縮約', gif_17),
    ('4. EBランキング補正', gif_18),
]
html=["<div style='display:grid; grid-template-columns: 1fr; gap: 24px;'>"]
for title,path in items:
    rel=path.relative_to(PROJECT_ROOT).as_posix()
    html.append(f"<section><h3>{title}</h3><p><code>{rel}</code></p><img src='../{rel}' style='max-width:960px;width:100%;border:1px solid #ddd;'></section>")
html.append('</div>')
display(HTML('\n'.join(html)))
'''))

cells.append(nbf.v4.new_code_cell(r'''# 6. Contact sheet for quick verification
from PIL import Image, ImageDraw

def read_gif_frame(path: Path, idx: int) -> Image.Image:
    reader=imageio.get_reader(path)
    try:
        n=reader.get_length(); arr=reader.get_data(min(max(idx,0),n-1))
    finally:
        reader.close()
    return Image.fromarray(arr).convert('RGB')

def make_contact_sheet(paths, out: Path) -> Path:
    labels=['first','middle','final']; cell_w,cell_h=410,285
    sheet=Image.new('RGB',(cell_w*3,cell_h*len(paths)),'white'); draw=ImageDraw.Draw(sheet)
    for r,path in enumerate(paths):
        reader=imageio.get_reader(path)
        try: n=reader.get_length()
        finally: reader.close()
        for c,idx in enumerate([0,n//2,n-1]):
            im=read_gif_frame(path,idx); im.thumbnail((380,230))
            x=c*cell_w+15; y=r*cell_h+42
            draw.text((x,r*cell_h+8),f'{path.name}\n{labels[c]}: frame {idx}',fill=(20,20,20))
            sheet.paste(im,(x,y))
    out.parent.mkdir(parents=True,exist_ok=True); sheet.save(out); print(f'saved {out}'); return out
contact_sheet=make_contact_sheet([gif_15,gif_16,gif_17,gif_18], FIG_DIR/'empirical_bayes_examples_contact_sheet.png')
contact_sheet
'''))

cells.append(nbf.v4.new_markdown_cell(r'''## 6. まとめ

経験ベイズの典型的な使い方は、以下の4つでかなり見通せます。

| 事例 | 生の推定 | EB prior | EBで起こること |
|---|---|---|---|
| 比率 | $y_j/n_j$ | Beta | 小標本の割合を全体率へ縮める |
| rate/count | $y_j/E_j$ | Gamma | 小標本の発生率を全体rateへ縮める |
| 平均 | $\bar y_j$ | Normal | 不確実な群平均を全体平均へ縮める |
| ランキング | 生の群平均順位 | Normal | 偶然の極端な上位/下位を補正する |

経験ベイズは「完全ベイズ」ではありません。ハイパーパラメータの不確実性を固定値として扱いがちです。ただし、少ないコードで部分プーリング・ランキング補正・安定化推定を体験しやすいので、階層モデル理解の入口として非常に有用です。
'''))

nb['cells']=cells
nbf.write(nb, NOTEBOOK_PATH)
print(NOTEBOOK_PATH)
