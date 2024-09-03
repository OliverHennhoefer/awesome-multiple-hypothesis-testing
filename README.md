# Awesome Multiple Hypothesis Testing
Extensive collection of resources on the topic of **multiple hypothesis testing**.

***

## 1 Publications

### 1.1 Philosophical

- [The Philosophy of Multiple Comparisons](https://projecteuclid.org/journals/statistical-science/volume-6/issue-1/The-Philosophy-of-Multiple-Comparisons/10.1214/ss/1177011945.full) [[Tuckey1991]](#tuckey1991)
- [John W. Tukey's Contributions to Multiple Comparisons](https://projecteuclid.org/journals/annals-of-statistics/volume-30/issue-6/John-W-Tukeys-contributions-to-multiple-comparisons/10.1214/aos/1043351247.full) [[Benjamini2002]](#benjamini2002)

### 1.2 Introductory

- [Multiple Testing](https://www.gs.washington.edu/academics/courses/akey/56008/lecture/lecture10.pdf) (Lecture Slides; [UW Genomics Sciences](https://www.gs.washington.edu/index.htm))
- [What is the proper way to apply the multiple comparison test?](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6193594/) [[Lee2018]](#lee2018)
- [Online Multiple Hypothesis Testing](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7615519/) [[Robertson2023]](#robertson23)
- [The Theory behind 'onineFDR'](https://bioconductor.org/packages/devel/bioc/vignettes/onlineFDR/inst/doc/theory.html#SAFFRON_gamma) (Website; Documentation)

### 1.3 Seminal: _Static_

#### Bonnferroni-Correction
- [Teoria statistica delle classi e calcolo delle probabilità](https://www.jstor.org/stable/23229706)
- [Multiple Comparisons Among Means](https://sci2s.ugr.es/keel/pdf/algorithm/articulo/1961-Bonferroni_Dunn-JASA.pdf) [[Dunn1961]](#dunn1961)
- [The Bonferonni and Šidák Corrections for Multiple Comparisons](https://personal.utdallas.edu/~Herve/Abdi-Bonferroni2007-pretty.pdf)

<details>
  <summary>Details</summary>

Algorithm for controlling the FWER in (static) hypothesis testing. The adjusted threshold $\alpha_i$ for $k$ tested hypotheses is calculated as:

$$\alpha_i = \frac{\alpha}{k}$$

</details>

#### [Benjamini-Hochberg Procedure](https://www.jstor.org/stable/2346101)

<details>
  <summary>Details</summary>

Algorithm for controlling the FDR in (static) hypothesis testing for _p_-values that are independent or with positive regression dependency on subsets:

- Given $\alpha$, sort all _p_-values $P_k$ and find the largest $k$ for $P_k \leq \frac{k}{m} \alpha$.
- Reject $\mathcal{H}_0$ for all $H_i$ for $i=1, 2, \ldots, k$.

[[BenjaminiHochberg1995]](#benjaminihochberg1995)

</details>

#### [Benjamini-Yekutieli Procedure](https://projecteuclid.org/journals/annals-of-statistics/volume-29/issue-4/The-control-of-the-false-discovery-rate-in-multiple-testing/10.1214/aos/1013699998.full)

<details>
  <summary>Details</summary>

Algorithm for controlling the FDR in (static) hypothesis testing for _p_-values under arbitrary dependence.
This modifies the threshold as obtained by Benjamini-Hochberg Procedure [[BenjaminiYekutieli2001]](#benjaminiyekutieli2001) as follows:

$$P_k \leq \frac{k}{m c(m)} \alpha$$

- The standard Benjamini-Hochberg Procedure can be recovered by $c(m)=1$ for independent or positively correlated _p_-values.
- Under arbitrary dependence $c(m)$ is defined as the _Harmonic_ number $c(m)=\sum^{m}{i=1}\frac{1}{i}$.

</details>

### 1.4 Seminal: _Sequential_

#### [SAFFRON](https://proceedings.mlr.press/v80/ramdas18a/ramdas18a.pdf)
<ins>S</ins>erial estimate of the <ins>A</ins>lpha <ins>F</ins>raction that is <ins>F</ins>utilely <ins>R</ins>ationed <ins>O</ins>n true <ins>N</ins>ull hypotheses. [[RamdasZrnic2018]](#ramdaszrnic2018)

<details>
  <summary>Details</summary>

Algorithm for controlling FDR in sequential (online) hypothesis testing for independent _p_-values that was proposed by [[RamdasZrnic2018]](#ramdaszrnic2018).

SAFFRON estimates the proportion of $\mathcal{H}_0$, i.e. adjusts the test levels $\alpha_i$ based on an estimate of the amount of alpha wealth that is allocated to testing true $\mathcal{H}_0$.
SAFFRON depends on the constants $w_0$ and $\lambda$, with $w_0$ as the initial alpha wealth, satisfying $0 \leq w_0 \leq \alpha$.
The parameter $\lambda \in (0,1)$ defines the threshold for a _candidate_ as SAFFRON never rejects _p_-values $\geq \lambda$.
Candidates are hypotheses that are more likely to be _discoveries_:

- At each time $t$, define the number of _candidates_ after the _j_-th rejection as

$`C_{j+} = C_{j+}(t) = \sum_{i = \tau_j + 1}^{t-1} C_i`$

with $C_t = 1\{p_t \leq \lambda \}$ as the indicator for candidacy.

- Subsequent test levels are chosen as $\alpha_t = \min\{ \lambda, \tilde{\alpha}_t\}$ with the exception

$`\alpha_1 = \min\{(1 - \lambda)\gamma_1 w_0, \lambda\}`$

and subsequent

$`\tilde{\alpha}_t = (1 - \lambda) [w_0 \gamma_{t-C_{0+}} + (\alpha - w_0)\gamma_{t-\tau_1-C_{1+}} +  \alpha \sum_{j \geq 2}  \gamma_{t - \tau_j- C_{j+}}]`$

Typically, $\gamma_j \propto j^{-1.6}$ is used as the $\gamma$ sequence.

</details>

#### [ADDIS](https://proceedings.neurips.cc/paper_files/paper/2019/file/1d6408264d31d453d556c60fe7d0459e-Paper.pdf)
An <ins>AD</ins>aptive algorithm that <ins>DIS</ins>cards conservative nulls. [[TianRamdas2019]](#tianramdas2019)

<details>
  <summary>Details</summary>

Algorithm for controlling FDR in sequential (online) hypothesis testing for independent _p_-values that was proposed by [[TianRamdas2019]](#tianramdas2019).
ADDIS iterates on SAFFRON by extending SAFFRONs **adaptivity in the fraction** of $\mathcal{H}_0$ by **adaptivity in the conservativeness** of $\mathcal{H}_0$.
ADDIS depends on the constants $W_0$, $\lambda$ and $\tau$, with $W_0$ as the initial alpha wealth, satisfying $0 \leq w_0 \leq \alpha$.
The new parameter $\tau \in (0,1]$ defines the threshold for discarding (conservative) _p_-values as _p_-values $\geq \tau$ are _discarded_ (i.e. not considered for testing, with no wealth invested).
As for SAFFRON, the parameter $\lambda \in [0,\tau)$  defines the threshold for _candidates_ as ADDIS will never reject _p_values $\geq \lambda$.

$`\alpha_t = \min\{\lambda, \tilde{\alpha}_t\}`$

$`\tilde{\alpha}_t = (\tau - \lambda)[w_0 \gamma_{S^t-C_{0+}} + (\alpha - w_0)\gamma_{S^t - \kappa_1^*-C_{1+}} +  \alpha \sum_{j \geq 2} \gamma_{S^t - \kappa_j^* - C_{j+}}`$

$`\kappa_j = \min\{i \in [t-1] : \sum_{k \leq i}  1 \{p_k \leq \alpha_k\} \geq j\}, \kappa_j^* = \sum_{i \leq \kappa_j} 1 \{p_i \leq \tau \}, S^t = \sum_{i < t} 1 \{p_i \leq \tau \}, C_{j+} = \sum_{i = \kappa_j + 1}^{t-1} 1\{p_i \leq \lambda\}`$

Typically, $\gamma_j \propto j^{-1.6}$ is used as the $\gamma$ sequence.

</details>

### 1.5 Seminal: _Batching_

[Batch$_{\text{BH}}$ and Batch$_{\text{Storey-BH}}$](https://par.nsf.gov/servlets/purl/10251949)

Interpolation algorithm between existing pure sequential (online) and static (offline) methods providing a trade-off between statistical power and temporal application. [[Zrnic2020]](#zrnic2020)

### 1.6 Applications and Modifications

#### 1.6.1 Anomaly Detection
- [Online False Discovery Rate Control for Anomaly Detection in Time-Series](https://proceedings.neurips.cc/paper_files/paper/2021/file/def130d0b67eb38b7a8f4e7121ed432c-Paper.pdf)
- [Online FDR Controlled Anomaly Detection for Streaming Time Series](https://kdd-milets.github.io/milets2019/papers/milets19_paper_6.pdf)
- [FDR Control for Online Anomaly Detection](https://hal.science/hal-04321622)

***

## 2 Presentations
- [NIPS21: Online False Discovery Rate Control for Anomaly Detection in Time-Series](https://slideslive.com/38968279/online-false-discovery-rate-control-for-anomaly-detection-in-time-series?ref=speaker-17986)

***

## 3 Software Packages
[R: onlineFDR](https://academic.oup.com/bioinformatics/article/35/20/4196/5380770) [[Robertson2019]](#robertson19)

### 3.1 Repositories

- [Original Repository: 'onlineFDR'](https://github.com/dsrobertson/onlineFDR) [[Robertson2019]](#robertson19)
- [Original Repository: SAFFRON](https://github.com/JINJINT/ADDIS) (see [[RamdasZrnic2018]](#ramdaszrnic2018))
- [Original Repository: ADDIS](https://github.com/JINJINT/ADDIS) (see [[TianRamdas2019]](#tianramdas2019))
- [Original Repository: Batching](https://github.com/jiangdaniel/BatchBH/blob/master/online.py) (see [[Zrnic2020]](#zrnic2020))

### 3.2 Miscellaneous

- [onlineFDRExplore](https://mrc-bsu.shinyapps.io/onlineFDRexplore/) (based on 'onlineFDR')
- [onlineFWERExplore](https://mrc-bsu.shinyapps.io/onlineFWERexplore/) (based on 'onlineFDR')

***
***

## 4 References
<a id="dunn1961">[Dunn1961]</a> Dunn, O. J. (1961). **Multiple Comparisons Among Means**. Journal of the American Statistical Association, 56(293), 52–64.

<a id="tuckey1991">[Tuckey1991]</a> Tukey, J. W. (1991). **The Philosophy of Multiple Comparisons**. Statistical Science, 6(1), 100-116.

<a id="benjaminihochberg1995">[BenjaminiHochberg1995]</a> Benjamini, Y., & Hochberg, Y. (1995). **Controlling the False Discovery Rate: A Practical and Powerful Approach to Multiple Testing**. Journal of the Royal Statistical Society. Series B (Methodological), 57(1), 289–300.

<a id="benjaminiyekutieli2001">[BenjaminiYekutieli2001]</a> Benjamini, Y., & Hochberg, Y. (1995). **Controlling the False Discovery Rate: A Practical and Powerful Approach to Multiple Testing**. Journal of the Royal Statistical Society. Series B (Methodological), 57(1), 289–300.

<a id="benjamini2002">[Benjamini2002]</a> Benjamini, Y., & Braun, H. (2002). **John W. Tukey's contributions to multiple comparisons**. The Annals of Statistics, 30(6), 1576-1594.

<a id="lee2018">[Lee2018]</a> Lee, S., & Lee, D. K. (2018). **What is the proper way to apply the multiple comparison test?**. Korean journal of anesthesiology, 71(5), 353–360.

<a id="robertson23">[Robertson2023]</a> Robertson, D. S., Wason, J. M. S., & Ramdas, A. (2023). **Online multiple hypothesis testing**. Statistical science : a review journal of the Institute of Mathematical Statistics, 38(4), 557–575.

<a id="robertson19">[Robertson2019]</a> Robertson DS, Liou L, Ramdas A, Karp NA (2022). **onlineFDR: Online error control**. R package 2.12.0.

<a id="ramdaszrnic2018">[RamdasZrnic2018]</a> Ramdas, A., Zrnic, T., Wainwright, M.J., & Jordan, M.I. (2018). **SAFFRON: an adaptive algorithm for online control of the false discovery rate**. International Conference on Machine Learning.

<a id="tianramdas2019">[TianRamdas2019]</a> Tian, J., & Ramdas, A. (2019). **ADDIS: An adaptive discarding algorithm for online FDR control with conservative nulls**. In H. Wallach, H. Larochelle, A. Beygelzimer, F. d'Alché-Buc, E. Fox, & R. Garnett (Eds.), Advances in Neural Information Processing Systems (Vol. 32). Curran Associates, Inc.

<a id="zrnic2020">[Zrnic2020]</a> Zrnic, T., Jiang, D., Ramdas, A., & Jordan, M.I. (2019). **The Power of Batching in Multiple Hypothesis Testing**. International Conference on Artificial Intelligence and Statistics.