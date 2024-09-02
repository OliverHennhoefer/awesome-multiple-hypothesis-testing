# Awesome Multiple Hypothesis Testing
Extensive collection of resources on the topic of **multiple hypothesis testing**.

***

## <ins>Publications</ins>

### <ins>Philosophical</ins>


### <ins>Introductional</ins>
[Online Multiple Hypothesis Testing](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7615519/) [[Robertson2023]](#robertson23)

[The Theory behind 'onineFDR'](https://bioconductor.org/packages/devel/bioc/vignettes/onlineFDR/inst/doc/theory.html#SAFFRON_gamma) (Website; Documentation)

### <ins>Seminal Publications</ins> (Static)

#### Bonnferroni-Correction

#### Benjamini-Hochberg Procedure

#### Benjamini-Hochberg Procedure

#### Benjamini-Hochberg Procedure

### <ins>Seminal Publications</ins> (Sequential)

#### [SAFFRON](https://proceedings.mlr.press/v80/ramdas18a/ramdas18a.pdf)
<ins>S</ins>erial estimate of the <ins>A</ins>lpha <ins>F</ins>raction that is <ins>F</ins>utilely <ins>R</ins>ationed <ins>O</ins>n true <ins>N</ins>ull hypotheses

<details>
  <summary>Details</summary>

Algorithm for controlling FDR in sequential (online) hypothesis testing for independent _p_-values that was proposed by [[RamdasZrnic2018]](#ramdaszrnic2018).

SAFFRON estimates the proportion of $\mathcal{H}_0$, i.e. adjusts the test levels $\alpha_i$ based on an estimate of the amount of alpha wealth that is allocated to testing true $\mathcal{H}_0$.
SAFFRON depends on the constants $w_0$ and $\lambda$, with $w_0$ as the initial alpha wealth, satisfying $0 \leq w_0 \leq \alpha$.
The parameter $\lambda \in (0,1)$ defines the threshold for a _candidate_ as SAFFRON never rejects _p_-values $\geq \lambda$.
Candidates are hypotheses that are more likely to be _discoveries_:

- At each time $t$, define the number of _candidates_ after the _j_-th rejection as

$$C_{j+} = C_{j+}(t) = \sum_{i = \tau_j + 1}^{t-1} C_i$$

with $C_t = 1\{p_t \leq \lambda \}$ as the indicator for candidacy.

- Subsequent test levels are chosen as $\alpha_t = \min\{ \lambda, \tilde{\alpha}_t\}$ with the exception

$$\alpha_1 = \min\{(1 - \lambda)\gamma_1 w_0, \lambda\}$$

and subsequent

$$\tilde{\alpha}_t = (1 - \lambda) [w_0 \gamma_{t-C_{0+}} + (\alpha - w_0)\gamma_{t-\tau_1-C_{1+}} +  \alpha \sum_{j \geq 2}  \gamma_{t - \tau_j- C_{j+}}]$$

Typically, $\gamma_j \propto j^{-1.6}$ is used as the $\gamma$ sequence.

</details>

#### [ADDIS](https://proceedings.neurips.cc/paper_files/paper/2019/file/1d6408264d31d453d556c60fe7d0459e-Paper.pdf)
An <ins>AD</ins>aptive algorithm that <ins>DIS</ins>cards conservative nulls.

<details>
  <summary>Details</summary>

Algorithm for controlling FDR in sequential (online) hypothesis testing for independent _p_-values that was proposed by [[TianRamdas2019]](#tianramdas2019).
ADDIS iterates on SAFFRON by extending SAFFRONs **adaptivity in the fraction** of $\mathcal{H}_0$ by **adaptivity in the conservativeness** of $\mathcal{H}_0$.
ADDIS depends on the constants $W_0$, $\lambda$ and $\tau$, with $W_0$ as the initial alpha wealth, satisfying $0 \leq w_0 \leq \alpha$.
The new parameter $\tau \in (0,1]$ defines the threshold for discarding (conservative) _p_-values as _p_-values $\geq \tau$ are _discarded_ (i.e. not considered for testing, with no wealth invested).
As for SAFFRON, the parameter $\lambda \in [0,\tau)$  defines the threshold for _candidates_ as ADDIS will never reject _p_values $\geq \lambda$.

$$\alpha_t = \min\{\lambda, \tilde{\alpha}_t\}$$

$$`\tilde{\alpha}_t = (\tau - \lambda)[w_0 \gamma_{S^t-C_{0+}} + (\alpha - w_0)\gamma_{S^t - \kappa_1^*-C_{1+}} +  \alpha \sum_{j \geq 2} \gamma_{S^t - \kappa_j^* - C_{j+}}`$$

$$\kappa_j = \min\{i \in [t-1] : \sum_{k \leq i}  1 \{p_k \leq \alpha_k\} \geq j\}, \kappa_j^* = \sum_{i \leq \kappa_j} 1 \{p_i \leq \tau \}, S^t = \sum_{i < t} 1 \{p_i \leq \tau \}, C_{j+} = \sum_{i = \kappa_j + 1}^{t-1} 1\{p_i \leq \lambda\}$$

Typically, $\gamma_j \propto j^{-1.6}$ is used as the $\gamma$ sequence.

</details>

***

## Presentations
[NIPS21: Online False Discovery Rate Control for Anomaly Detection in Time-Series](https://slideslive.com/38968279/online-false-discovery-rate-control-for-anomaly-detection-in-time-series?ref=speaker-17986)

***

## Software Packages
[R: onlineFDR](https://academic.oup.com/bioinformatics/article/35/20/4196/5380770) [[Robertson2019]](#robertson19)

### Repositories

[Original Repository: SAFFRON](https://github.com/JINJINT/ADDIS) (see [[RamdasZrnic2018]](#ramdaszrnic2018))
[Original Repository: ADDIS](https://github.com/JINJINT/ADDIS) (see [[TianRamdas2019]](#tianramdas2019))

***
***

## References

<a id="robertson23">[Robertson2023]</a> Robertson, D. S., Wason, J. M. S., & Ramdas, A. (2023). **Online multiple hypothesis testing**. Statistical science : a review journal of the Institute of Mathematical Statistics, 38(4), 557–575.

<a id="robertson19">[Robertson2019]</a> Robertson DS, Liou L, Ramdas A, Karp NA (2022). onlineFDR: Online error control. R package 2.12.0.

<a id="ramdaszrnic2018">[RamdasZrnic2018]</a> Ramdas, A., Zrnic, T., Wainwright, M.J., & Jordan, M.I. (2018). **SAFFRON: an adaptive algorithm for online control of the false discovery rate**. International Conference on Machine Learning.

<a id="tianramdas2019">[TianRamdas2019]</a> Tian, J., & Ramdas, A. (2019). **ADDIS: An adaptive discarding algorithm for online FDR control with conservative nulls**. In H. Wallach, H. Larochelle, A. Beygelzimer, F. d'Alché-Buc, E. Fox, & R. Garnett (Eds.), Advances in Neural Information Processing Systems (Vol. 32). Curran Associates, Inc.
