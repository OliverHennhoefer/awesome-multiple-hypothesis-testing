# Awesome Multiple Hypothesis Testing [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

Multiple hypothesis testing controls errors when drawing conclusions from a family or stream of statistical tests.

A curated reading map from classical simultaneous inference to modern false discovery control, with philosophical context, foundational papers, methodological extensions, and implementations. Research entries link to published articles in refereed journals or reviewed conference proceedings. Authoritative monographs are explicitly labelled exceptions. Software links are implementation resources, not independent evidence of statistical validity. See the [selection policy](CONTRIBUTING.md#selection-policy) for the narrowly defined exception for expert preprints and reports; none are currently included.

## Contents

- [Orientation](#orientation)
- [Philosophy and Foundations](#philosophy-and-foundations)
- [Reviews and Tutorials](#reviews-and-tutorials)
- [Seminal Papers](#seminal-papers)
- [Familywise Error Control](#familywise-error-control)
  - [Classical Comparisons and Stepwise Procedures](#classical-comparisons-and-stepwise-procedures)
  - [Resampling and General Principles](#resampling-and-general-principles)
  - [Gatekeeping and Graphical Procedures](#gatekeeping-and-graphical-procedures)
- [Global Tests and P-Value Combination](#global-tests-and-p-value-combination)
- [False Discovery Rate Control](#false-discovery-rate-control)
  - [Dependence and General Theory](#dependence-and-general-theory)
  - [Adaptation and Null Proportion Estimation](#adaptation-and-null-proportion-estimation)
  - [Weights and Covariate Information](#weights-and-covariate-information)
- [Empirical Bayes and Local FDR](#empirical-bayes-and-local-fdr)
- [Structured and Ordered Hypotheses](#structured-and-ordered-hypotheses)
- [Selective Inference and Simultaneous FDP Bounds](#selective-inference-and-simultaneous-fdp-bounds)
- [Discrete Tests and Conservative P-Values](#discrete-tests-and-conservative-p-values)
- [Replicability and Directional Errors](#replicability-and-directional-errors)
- [Variable Selection and Knockoffs](#variable-selection-and-knockoffs)
- [Online Multiple Testing](#online-multiple-testing)
  - [Alpha Investing and Adaptive FDR](#alpha-investing-and-adaptive-fdr)
  - [Batches, Asynchrony, and Decision Deadlines](#batches-asynchrony-and-decision-deadlines)
  - [Online FWER, FDX, and Confidence Statements](#online-fwer-fdx-and-confidence-statements)
- [Sequential Testing and Adaptive Sampling](#sequential-testing-and-adaptive-sampling)
- [E-Values and Anytime-Valid Inference](#e-values-and-anytime-valid-inference)
- [Applications](#applications)
  - [Genomics and Proteomics](#genomics-and-proteomics)
  - [Neuroimaging and Spatial Inference](#neuroimaging-and-spatial-inference)
  - [Anomaly Detection and Conformal Selection](#anomaly-detection-and-conformal-selection)
  - [Experiments and Clinical Trials](#experiments-and-clinical-trials)
- [Authoritative Monographs](#authoritative-monographs)
- [Software](#software)
  - [R](#r)
  - [Python](#python)
  - [Julia](#julia)
  - [Research Implementations](#research-implementations)

## Orientation

Let $V$ be the number of false rejections and $R$ the total number of rejections. The false discovery proportion is $\mathrm{FDP}=V/\max(R,1)$; it is zero when nothing is rejected.

| Target                                               | What is controlled                                                                        | Reading route                                     |
| ---------------------------------------------------- | ----------------------------------------------------------------------------------------- | ------------------------------------------------- |
| Familywise error rate, FWER                          | The probability of at least one false rejection, $\Pr(V\geq1)$.                           | Seminal papers, then familywise methods.          |
| False discovery rate, FDR                            | The expected false discovery proportion, $\mathbb{E}(\mathrm{FDP})$.                      | BH and BY in seminal papers, then FDR extensions. |
| Generalized FWER and false discovery exceedance, FDX | The probability of at least $k$ false rejections, or of FDP exceeding a chosen tolerance. | General principles and simultaneous FDP bounds.   |
| Selective confidence statements                      | Coverage or false coverage rate for parameters selected after seeing the data.            | Selective inference.                              |
| Growing families of hypotheses                       | Error control as new hypotheses arrive, possibly in overlapping experiments or batches.   | Online multiple testing.                          |
| Optional stopping within experiments                 | Valid inference when sample sizes or stopping times depend on the observations.           | E-values and anytime-valid inference.             |

For a first pass, read Shaffer or Goeman–Solari in reviews, Holm and BH in seminal papers, and Robertson–Wason–Ramdas before the online literature. Papers appear once, under their main contribution; within sections, the order is generally chronological.

**Check the guarantee before choosing a method.** FDR is not the marginal FDR, which uses a ratio of expectations, nor the posterior probability that one particular discovery is false. Positive pairwise correlation is not the same as the positive regression dependence condition used in BH theory. A global-null rejection does not identify individual false nulls. Fixed-time control does not automatically extend to arbitrary stopping times. The cited papers specify the required dependence, exchangeability, model, and selection assumptions.

## Philosophy and Foundations

These papers frame the debate about the family of claims, exploratory versus confirmatory analysis, and the consequences of errors. Including a critical perspective does not imply that its recommendation applies to every study.

- [No Adjustments Are Needed for Multiple Comparisons](https://doi.org/10.1097/00001648-199001000-00010) - Rothman (1990, *Epidemiology*). Influential argument against routine adjustment; useful for understanding the scientific objectives behind the debate.
- [The Philosophy of Multiple Comparisons](https://doi.org/10.1214/ss/1177011945) - Tukey (1991, *Statistical Science*). Foundational discussion of which comparisons belong together and how simultaneous inference serves scientific questions.
- [Multiple Comparisons and Related Issues in the Interpretation of Epidemiologic Data](https://doi.org/10.1093/oxfordjournals.aje.a117737) - Savitz and Olshan (1995, *American Journal of Epidemiology*). Examines multiplicity alongside study context, prior evidence, and interpretation.
- [What's Wrong with Bonferroni Adjustments](https://doi.org/10.1136/bmj.316.7139.1236) - Perneger (1998, *BMJ*). Widely discussed critique of indiscriminate Bonferroni adjustment and its effects on interpretation and power.
- [Adjusting for Multiple Testing—When and How?](https://doi.org/10.1016/S0895-4356(00)00314-0) - Bender and Lange (2001, *Journal of Clinical Epidemiology*). Connects adjustment decisions to confirmatory and exploratory goals.
- [John W. Tukey's Contributions to Multiple Comparisons](https://doi.org/10.1214/aos/1043351247) - Benjamini and Braun (2002, *The Annals of Statistics*). Historical account of Tukey's ideas and their influence on modern multiplicity control.
- [On Selection and Conditioning in Multiple Testing and Selective Inference](https://doi.org/10.1093/biomet/asad078) - Goeman and Solari (2024, *Biometrika*). Examines when conditioning on selection helps and when inference over the original hypothesis universe is more powerful.

## Reviews and Tutorials

- [Multiple Hypothesis Testing](https://doi.org/10.1146/annurev.ps.46.020195.003021) - Shaffer (1995, *Annual Review of Psychology*). Broad introduction to simultaneous inference, ordered p-value procedures, and comparisons of means.
- [Multiple Hypothesis Testing in Microarray Experiments](https://doi.org/10.1214/ss/1056397487) - Dudoit, Shaffer, and Boldrick (2003, *Statistical Science*). Reviews error criteria, adjusted p-values, and resampling in high-dimensional testing.
- [A Review of Modern Multiple Hypothesis Testing, with Particular Attention to the False Discovery Proportion](https://doi.org/10.1177/0962280206079046) - Farcomeni (2008, *Statistical Methods in Medical Research*). Surveys FWER, FDR, FDP, dependence, and resampling approaches.
- [Multiple Hypothesis Testing in Genomics](https://doi.org/10.1002/sim.6082) - Goeman and Solari (2014, *Statistics in Medicine*). Accessible treatment of choosing an error criterion and avoiding common interpretation mistakes.
- [What Is the Proper Way to Apply the Multiple Comparison Test?](https://doi.org/10.4097/kja.d.18.00242) - Lee and Lee (2018, *Korean Journal of Anesthesiology*). Practical introduction to post-hoc comparisons; also consult the publication's [correction](https://doi.org/10.4097/kja.d.18.00242.e1).
- [A Practical Guide to Methods Controlling False Discoveries in Computational Biology](https://doi.org/10.1186/s13059-019-1716-1) - Korthauer et al. (2019, *Genome Biology*). Reproducible comparison of classical and covariate-aware FDR methods across simulations and biological datasets.
- [Online Multiple Hypothesis Testing](https://doi.org/10.1214/23-STS901) - Robertson, Wason, and Ramdas (2023, *Statistical Science*). Main entry point for online FDR, FWER, asynchronous testing, batching, and implementation.
- [Replicability Across Multiple Studies](https://doi.org/10.1214/23-STS892) - Bogomolov and Heller (2023, *Statistical Science*). Explains how replicability claims differ from meta-analytic evidence of an effect somewhere.

## Seminal Papers

A deliberately short historical spine. Further landmarks appear in their specialist sections.

- [Comparing Individual Means in the Analysis of Variance](https://doi.org/10.2307/3001913) - Tukey (1949, *Biometrics*). Establishes the simultaneous comparison of means that underlies Tukey-style procedures.
- [A Method for Judging All Contrasts in the Analysis of Variance](https://doi.org/10.2307/2333100) - Scheffé (1953, *Biometrika*). Protects all linear contrasts, including contrasts chosen after inspecting the data.
- [Multiple Comparisons among Means](https://doi.org/10.1080/01621459.1961.10482090) - Dunn (1961, *Journal of the American Statistical Association*). Classical treatment of Bonferroni-based simultaneous comparisons.
- [On Closed Testing Procedures with Special Reference to Ordered Analysis of Variance](https://doi.org/10.1093/biomet/63.3.655) - Marcus, Peritz, and Gabriel (1976, *Biometrika*). Introduces closed testing, a general route from intersection tests to strong FWER control.
- [A Simple Sequentially Rejective Multiple Test Procedure](https://www.jstor.org/stable/4615733) - Holm (1979, *Scandinavian Journal of Statistics*). Step-down Bonferroni procedure with strong FWER control under arbitrary dependence.
- [An Improved Bonferroni Procedure for Multiple Tests of Significance](https://doi.org/10.1093/biomet/73.3.751) - Simes (1986, *Biometrika*). Global intersection test underlying several stepwise methods; validity requires suitable dependence conditions.
- [Controlling the False Discovery Rate: A Practical and Powerful Approach to Multiple Testing](https://doi.org/10.1111/j.2517-6161.1995.tb02031.x) - Benjamini and Hochberg (1995, *Journal of the Royal Statistical Society B*). Introduces FDR and the BH step-up procedure, with the original guarantee under independence.
- [The Control of the False Discovery Rate in Multiple Testing under Dependency](https://doi.org/10.1214/aos/1013699998) - Benjamini and Yekutieli (2001, *The Annals of Statistics*). Extends BH to positive regression dependence and gives the BY harmonic correction for arbitrary dependence.
- [A Direct Approach to False Discovery Rates](https://doi.org/10.1111/1467-9868.00346) - Storey (2002, *Journal of the Royal Statistical Society B*). Pioneers adaptive FDR estimation through estimation of the proportion of true null hypotheses.
- [Alpha-Investing: A Procedure for Sequential Control of Expected False Discoveries](https://doi.org/10.1111/j.1467-9868.2007.00643.x) - Foster and Stine (2008, *Journal of the Royal Statistical Society B*). Introduces reusable alpha wealth for hypothesis streams; the original guarantee concerns a modified marginal FDR.
- [Controlling the False Discovery Rate via Knockoffs](https://doi.org/10.1214/15-AOS1337) - Barber and Candès (2015, *The Annals of Statistics*). Introduces synthetic control variables for finite-sample FDR control in fixed-design Gaussian linear regression.

## Familywise Error Control

Bonferroni, Holm, and the closure principle are introduced in seminal papers. Strong control applies under every configuration of true and false nulls; weak control only protects the global null.

### Classical Comparisons and Stepwise Procedures

- [A Multiple Comparison Procedure for Comparing Several Treatments with a Control](https://doi.org/10.1080/01621459.1955.10501294) - Dunnett (1955, *Journal of the American Statistical Association*). Simultaneous comparisons against a common control, exploiting their joint distribution.
- [Multiple Comparisons Using Rank Sums](https://doi.org/10.1080/00401706.1964.10490181) - Dunn (1964, *Technometrics*). Rank-based pairwise comparisons using a shared ranking, with asymptotic calibration and treatment of ties.
- [Rectangular Confidence Regions for the Means of Multivariate Normal Distributions](https://doi.org/10.1080/01621459.1967.10482935) - Šidák (1967, *Journal of the American Statistical Association*). Develops simultaneous rectangular confidence regions and the correction associated with Šidák's inequality.
- [Pairwise Multiple Comparison Procedures with Unequal N's and/or Variances: A Monte Carlo Study](https://doi.org/10.3102/10769986001002113) - Games and Howell (1976, *Journal of Educational Statistics*). Studies pairwise mean comparisons under unequal variances and sample sizes, including the Games–Howell approach.
- [Modified Sequentially Rejective Multiple Test Procedures](https://doi.org/10.1080/01621459.1986.10478341) - Shaffer (1986, *Journal of the American Statistical Association*). Improves step-down testing by exploiting logical restrictions among hypotheses.
- [A Sharper Bonferroni Procedure for Multiple Tests of Significance](https://doi.org/10.1093/biomet/75.4.800) - Hochberg (1988, *Biometrika*). Step-up FWER procedure under independence or dependence conditions supporting the relevant Simes inequalities.
- [A Stagewise Rejective Multiple Test Procedure Based on a Modified Bonferroni Test](https://doi.org/10.1093/biomet/75.2.383) - Hommel (1988, *Biometrika*). Closed-Simes-based improvement over simpler stepwise procedures under appropriate dependence assumptions.
- [Simultaneous Inference in General Parametric Models](https://doi.org/10.1002/bimj.200810425) - Hothorn, Bretz, and Westfall (2008, *Biometrical Journal*). Unifies simultaneous tests and confidence intervals for model contrasts; methodological basis of multcomp.
- [Hommel's Procedure in Linear Time](https://doi.org/10.1002/bimj.201700316) - Meijer, Krebs, and Goeman (2019, *Biometrical Journal*). Efficient computation makes Hommel's procedure practical for large families.

### Resampling and General Principles

- [Exact and Approximate Stepdown Methods for Multiple Hypothesis Testing](https://doi.org/10.1198/016214504000000539) - Romano and Wolf (2005, *Journal of the American Statistical Association*). Resampling-based step-down tests that account for dependence among statistics.
- [Generalizations of the Familywise Error Rate](https://doi.org/10.1214/009053605000000084) - Lehmann and Romano (2005, *The Annals of Statistics*). Develops procedures controlling generalized FWER and the probability of excessive false discovery proportions.
- [Stepup Procedures for Control of Generalizations of the Familywise Error Rate](https://doi.org/10.1214/009053606000000461) - Romano and Shaikh (2006, *The Annals of Statistics*). Step-up methods for generalized error criteria under broad dependence conditions.
- [Exceedance Control of the False Discovery Proportion](https://doi.org/10.1198/016214506000000339) - Genovese and Wasserman (2006, *Journal of the American Statistical Association*). Controls the probability that the realized FDP exceeds a specified tolerance.
- [Multiple Testing with Minimal Assumptions](https://doi.org/10.1002/bimj.200710456) - Westfall and Troendle (2008, *Biometrical Journal*). Clarifies assumptions needed for permutation-based strong FWER control.
- [The Sequential Rejection Principle of Familywise Error Control](https://doi.org/10.1214/10-AOS829) - Goeman and Solari (2010, *The Annals of Statistics*). General proof principle unifying stepwise, graphical, and other sequentially rejective procedures.
- [Permutation P-values Should Never Be Zero: Calculating Exact P-values When Permutations Are Randomly Drawn](https://doi.org/10.2202/1544-6115.1585) - Phipson and Smyth (2010, *Statistical Applications in Genetics and Molecular Biology*). Explains valid Monte Carlo p-values, particularly important when many small p-values drive multiplicity procedures.
- [Efficient Computation of Adjusted P-values for Resampling-Based Stepdown Multiple Testing](https://doi.org/10.1016/j.spl.2016.02.012) - Romano and Wolf (2016, *Statistics & Probability Letters*). Practical algorithm for computing resampling-adjusted p-values.
- [Familywise Error Rate Control by Interactive Unmasking](https://proceedings.mlr.press/v119/duan20d.html) - Duan, Ramdas, and Wasserman (2020, *ICML*). The i-FWER procedure permits adaptive guidance while preserving familywise control through a prescribed masking protocol.

### Gatekeeping and Graphical Procedures

- [Gatekeeping Strategies for Clinical Trials That Do Not Require All Primary Effects to Be Significant](https://doi.org/10.1002/sim.1526) - Dmitrienko, Offen, and Westfall (2003, *Statistics in Medicine*). Controls FWER across prioritized primary and secondary endpoint families.
- [The Fallback Procedure for Evaluating a Single Family of Hypotheses](https://doi.org/10.1080/10543400500265660) - Wiens and Dmitrienko (2005, *Journal of Biopharmaceutical Statistics*). Allocates and recycles significance levels across an ordered family.
- [A Graphical Approach to Sequentially Rejective Multiple Test Procedures](https://doi.org/10.1002/sim.3495) - Bretz, Maurer, Brannath, and Posch (2009, *Statistics in Medicine*). Represents alpha allocation and recycling with directed weighted graphs.
- [A Recycling Framework for the Construction of Bonferroni-Based Multiple Tests](https://doi.org/10.1002/sim.3513) - Burman, Sonesson, and Guilbaud (2009, *Statistics in Medicine*). General framework for recycling local levels while preserving familywise control.
- [Graphical Approaches for Multiple Comparison Procedures Using Weighted Bonferroni, Simes, or Parametric Tests](https://doi.org/10.1002/bimj.201000239) - Bretz et al. (2011, *Biometrical Journal*). Extends graphical testing beyond Bonferroni local tests.

## Global Tests and P-Value Combination

These methods test intersection or global hypotheses. Further closure or selection arguments are needed to turn a global rejection into individual discoveries.

- [A Method for Combining Non-Independent, One-Sided Tests of Significance](https://doi.org/10.2307/2529826) - Brown (1975, *Biometrics*). Moment-based approximation to Fisher's combined statistic for dependent tests; an approximation rather than a universal exact guarantee.
- [Truncated Product Method for Combining P-values](https://doi.org/10.1002/gepi.0042) - Zaykin, Zhivotovsky, Westfall, and Weir (2002, *Genetic Epidemiology*). Combines only p-values below a threshold to emphasize a subset of signals.
- [Higher Criticism for Detecting Sparse Heterogeneous Mixtures](https://doi.org/10.1214/009053604000000265) - Donoho and Jin (2004, *The Annals of Statistics*). Global detection of sparse, weak signals and the associated asymptotic detection boundary.
- [Cauchy Combination Test: A Powerful Test with Analytic P-value Calculation under Arbitrary Dependency Structures](https://doi.org/10.1080/01621459.2018.1554485) - Liu and Xie (2020, *Journal of the American Statistical Association*). Analytic tail approximation under the paper's conditions; not an unrestricted finite-sample guarantee.
- [Combining P-values via Averaging](https://doi.org/10.1093/biomet/asaa027) - Vovk and Wang (2020, *Biometrika*). Calibrates generalized means of p-values for valid combination under arbitrary dependence.
- [Admissible Ways of Merging P-values under Arbitrary Dependence](https://doi.org/10.1214/21-AOS2109) - Vovk, Wang, and Wang (2022, *The Annals of Statistics*). Characterizes and improves valid p-value merging rules without independence assumptions.

## False Discovery Rate Control

The original BH, BY, and Storey papers are in seminal papers. Distinguish proven finite-sample control, asymptotic guarantees, and estimation of an error rate after fixing a rejection threshold.

### Dependence and General Theory

- [Some Probability Inequalities for Ordered MTP2 Random Variables: A Proof of the Simes Conjecture](https://doi.org/10.1214/aos/1028144846) - Sarkar (1998, *The Annals of Statistics*). Establishes Simes-type inequalities under a strong positive dependence condition.
- [Resampling-Based False Discovery Rate Controlling Multiple Test Procedures for Correlated Test Statistics](https://doi.org/10.1016/S0378-3758(99)00041-5) - Yekutieli and Benjamini (1999, *Journal of Statistical Planning and Inference*). Early resampling approach to FDR control that uses dependence information.
- [Some Results on False Discovery Rate in Stepwise Multiple Testing Procedures](https://doi.org/10.1214/aos/1015362192) - Sarkar (2002, *The Annals of Statistics*). Develops FDR theory for stepwise procedures under dependence.
- [A Stochastic Process Approach to False Discovery Control](https://doi.org/10.1214/009053604000000283) - Genovese and Wasserman (2004, *The Annals of Statistics*). Studies the stochastic behavior of false discoveries and asymptotic threshold selection.
- [Two Simple Sufficient Conditions for FDR Control](https://doi.org/10.1214/08-EJS180) - Blanchard and Roquain (2008, *Electronic Journal of Statistics*). Separates self-consistency and dependence control, providing a reusable framework for deriving FDR procedures.
- [Control of the False Discovery Rate under Dependence Using the Bootstrap and Subsampling](https://doi.org/10.1007/s11749-008-0126-6) - Romano, Shaikh, and Wolf (2008, *TEST*). Uses resampling to accommodate dependence, with explicit asymptotic conditions.
- [Conditional Calibration for False Discovery Rate Control under Dependence](https://doi.org/10.1214/21-AOS2137) - Fithian and Lei (2022, *The Annals of Statistics*). Adapts rejection thresholds to known dependence through conditional calibration.
- [False Discovery Rate Control with Compound P-values](https://doi.org/10.1093/jrsssb/qkag116) - Barber and Samworth (2026, *Journal of the Royal Statistical Society B*). Investigates p-values that satisfy null validity on average; ordinary BH guarantees do not transfer unchanged.

### Adaptation and Null Proportion Estimation

- [The Positive False Discovery Rate: A Bayesian Interpretation and the Q-value](https://doi.org/10.1214/aos/1074290335) - Storey (2003, *The Annals of Statistics*). Develops pFDR and q-values and explains their relationship to Bayesian quantities.
- [Strong Control, Conservative Point Estimation and Simultaneous Conservative Consistency of False Discovery Rates: A Unified Approach](https://doi.org/10.1111/j.1467-9868.2004.00439.x) - Storey, Taylor, and Siegmund (2004, *Journal of the Royal Statistical Society B*). Establishes guarantees for adaptive procedures and conservative FDR estimates.
- [Adaptive Linear Step-up Procedures That Control the False Discovery Rate](https://doi.org/10.1093/biomet/93.3.491) - Benjamini, Krieger, and Yekutieli (2006, *Biometrika*). Two-stage adaptive testing that estimates the number of true nulls while retaining control under stated assumptions.
- [An Adaptive Step-down Procedure with Proven FDR Control under Independence](https://doi.org/10.1214/07-AOS586) - Gavrilov, Benjamini, and Sarkar (2009, *The Annals of Statistics*). Adaptive step-down alternative with a finite-sample independence guarantee.
- [Adaptive False Discovery Rate Control under Independence and Dependence](https://www.jmlr.org/papers/v10/blanchard09a.html) - Blanchard and Roquain (2009, *Journal of Machine Learning Research*). Constructs adaptive procedures with explicit guarantees under independence, positive dependence, and unspecified dependence.

### Weights and Covariate Information

- [Multiple Hypotheses Testing with Weights](https://doi.org/10.1111/1467-9469.00072) - Benjamini and Hochberg (1997, *Scandinavian Journal of Statistics*). Incorporates prespecified scientific priorities into multiple testing.
- [False Discovery Control with P-value Weighting](https://doi.org/10.1093/biomet/93.3.509) - Genovese, Roeder, and Wasserman (2006, *Biometrika*). Develops weighted FDR procedures and power considerations for informative weights.
- [False Discovery Rate Regression: An Application to Neural Synchrony Detection in Primary Visual Cortex](https://doi.org/10.1080/01621459.2014.990973) - Scott et al. (2015, *Journal of the American Statistical Association*). Models variation in signal prevalence using covariates within an empirical Bayes framework.
- [Data-Driven Hypothesis Weighting Increases Detection Power in Genome-Scale Multiple Testing](https://doi.org/10.1038/nmeth.3885) - Ignatiadis, Klaus, Zaugg, and Huber (2016, *Nature Methods*). Introduces independent hypothesis weighting, using informative covariates independent of null p-values.
- [AdaPT: An Interactive Procedure for Multiple Testing with Side Information](https://doi.org/10.1111/rssb.12274) - Lei and Fithian (2018, *Journal of the Royal Statistical Society B*). Masking-based adaptive thresholds that let flexible models use side information without unrestricted reuse of p-values.
- [A Direct Approach to Estimating False Discovery Rates Conditional on Covariates](https://doi.org/10.7717/peerj.6035) - Boca and Leek (2018, *PeerJ*). Regression-based estimation of the null proportion conditional on auxiliary information.
- [Multiple Testing with the Structure-Adaptive Benjamini–Hochberg Algorithm](https://doi.org/10.1111/rssb.12298) - Li and Barber (2019, *Journal of the Royal Statistical Society B*). SABHA adapts to structured null proportions with explicit restrictions on model complexity.
- [Covariate Powered Cross-Weighted Multiple Testing](https://doi.org/10.1111/rssb.12411) - Ignatiadis and Huber (2021, *Journal of the Royal Statistical Society B*). Cross-weighting framework and theoretical guarantees for learning hypothesis weights.

## Empirical Bayes and Local FDR

Local FDR, tail-area FDR, false sign rates, and frequentist FDR control answer different questions. Estimated posterior quantities require their model and estimation assumptions.

- [Empirical Bayes Analysis of a Microarray Experiment](https://doi.org/10.1198/016214501753382129) - Efron, Tibshirani, Storey, and Tusher (2001, *Journal of the American Statistical Association*). Foundational empirical Bayes treatment of large-scale testing and local false discovery rates.
- [Large-Scale Simultaneous Hypothesis Testing: The Choice of a Null Hypothesis](https://doi.org/10.1198/016214504000000089) - Efron (2004, *Journal of the American Statistical Association*). Explains why theoretical and empirical null distributions can produce very different conclusions.
- [Correlation and Large-Scale Simultaneous Significance Testing](https://doi.org/10.1198/016214506000001211) - Efron (2007, *Journal of the American Statistical Association*). Investigates dependence and the accuracy of large-scale significance analyses.
- [Oracle and Adaptive Compound Decision Rules for False Discovery Rate Control](https://doi.org/10.1198/016214507000000545) - Sun and Cai (2007, *Journal of the American Statistical Association*). Decision-theoretic development of efficient testing using local false discovery information.
- [fdrtool: A Versatile R Package for Estimating Local and Tail Area-Based False Discovery Rates](https://doi.org/10.1093/bioinformatics/btn209) - Strimmer (2008, *Bioinformatics*). Unified empirical-null and false-discovery estimation from several kinds of test statistics.
- [Large-Scale Multiple Testing under Dependence](https://doi.org/10.1111/j.1467-9868.2008.00694.x) - Sun and Cai (2009, *Journal of the Royal Statistical Society B*). Exploits dependence through a hidden Markov model and compound decision rules.
- [Bayes and Empirical-Bayes Multiplicity Adjustment in the Variable-Selection Problem](https://doi.org/10.1214/10-AOS792) - Scott and Berger (2010, *The Annals of Statistics*). Explains when Bayesian model-selection priors produce multiplicity adjustment and when empirical Bayes approaches differ.
- [False Discovery Rates: A New Deal](https://doi.org/10.1093/biostatistics/kxw041) - Stephens (2017, *Biostatistics*). Adaptive shrinkage uses effect estimates and standard errors, emphasizing local false sign rates.

## Structured and Ordered Hypotheses

Here, structure means groups, trees, directed acyclic graphs, or a prespecified ordering. An ordered offline list is different from an indefinite online stream.

- [Hierarchical Testing of Variable Importance](https://doi.org/10.1093/biomet/asn007) - Meinshausen (2008, *Biometrika*). Tests successively finer clusters of variables with FWER control simultaneously across resolution levels.
- [Hierarchical False Discovery Rate–Controlling Methodology](https://doi.org/10.1198/016214507000001373) - Yekutieli (2008, *Journal of the American Statistical Association*). Hierarchical testing that follows discoveries down a tree, with explicitly defined error criteria.
- [Simultaneous Testing of Grouped Hypotheses: Finding Needles in Multiple Haystacks](https://doi.org/10.1198/jasa.2009.tm08415) - Cai and Sun (2009, *Journal of the American Statistical Association*). Uses differences between groups to improve large-scale testing efficiency.
- [Selective Inference on Multiple Families of Hypotheses](https://doi.org/10.1111/rssb.12028) - Benjamini and Bogomolov (2014, *Journal of the Royal Statistical Society B*). Adjusts inference within selected families to account for the selection of those families.
- [Sequential Selection Procedures and False Discovery Rate Control](https://doi.org/10.1111/rssb.12122) - G'Sell, Wager, Chouldechova, and Tibshirani (2016, *Journal of the Royal Statistical Society B*). ForwardStop and StrongStop rules for ordered model-selection hypotheses.
- [Accumulation Tests for FDR Control in Ordered Hypothesis Testing](https://doi.org/10.1080/01621459.2016.1180989) - Li and Barber (2017, *Journal of the American Statistical Association*). General framework for selecting a prefix of an ordered sequence while controlling false discoveries.
- [A Sequential Algorithm for False Discovery Rate Control on Directed Acyclic Graphs](https://doi.org/10.1093/biomet/asy066) - Ramdas, Chen, Wainwright, and Jordan (2019, *Biometrika*). DAGGER respects logical ordering constraints among hypotheses on a DAG.
- [A Unified Treatment of Multiple Testing with Prior Knowledge Using the P-filter](https://doi.org/10.1214/18-AOS1765) - Ramdas, Barber, Wainwright, and Jordan (2019, *The Annals of Statistics*). Simultaneously controls FDR at multiple grouping resolutions, with weights and prior information.
- [A General Interactive Framework for False Discovery Rate Control under Structural Constraints](https://doi.org/10.1093/biomet/asaa064) - Lei, Ramdas, and Fithian (2021, *Biometrika*). STAR uses masked information to let analysts adaptively refine a structured rejection set while maintaining finite-sample FDR control.
- [Filtering the Rejection Set While Preserving False Discovery Rate Control](https://doi.org/10.1080/01621459.2021.1920958) - Katsevich, Sabatti, and Bogomolov (2023, *Journal of the American Statistical Association*). Focused BH accounts for a filtering rule applied to discoveries; arbitrary post-hoc filtering can invalidate ordinary FDR control.

## Selective Inference and Simultaneous FDP Bounds

These methods address inference after choosing models, parameters, or subsets. They control different objects: conditional coverage, simultaneous coverage, false coverage rate, or simultaneous FDP bounds.

- [False Discovery Rate–Adjusted Multiple Confidence Intervals for Selected Parameters](https://doi.org/10.1198/016214504000001907) - Benjamini and Yekutieli (2005, *Journal of the American Statistical Association*). Introduces false coverage-statement rate control for intervals reported after selection.
- [Multiple Testing for Exploratory Research](https://doi.org/10.1214/11-STS356) - Goeman and Solari (2011, *Statistical Science*). Closed testing provides simultaneous bounds on false discoveries in subsets chosen after examining the data.
- [Valid Post-Selection Inference](https://doi.org/10.1214/12-AOS1077) - Berk et al. (2013, *The Annals of Statistics*). PoSI constructs simultaneous guarantees that remain valid after model selection.
- [Exact Post-Selection Inference, with Application to the Lasso](https://doi.org/10.1214/15-AOS1371) - Lee, Sun, Sun, and Taylor (2016, *The Annals of Statistics*). Conditional inference after selection events expressible as polyhedral constraints.
- [Post Hoc Confidence Bounds on False Positives Using Reference Families](https://doi.org/10.1214/19-AOS1847) - Blanchard, Neuvial, and Roquain (2020, *The Annals of Statistics*). Reference families allow simultaneous false-positive bounds for data-chosen subsets.
- [Simultaneous High-Probability Bounds on the False Discovery Proportion in Structured, Regression and Online Settings](https://doi.org/10.1214/19-AOS1938) - Katsevich and Ramdas (2020, *The Annals of Statistics*). Uniform FDP bounds support exploration across multiple rejection sets.
- [Only Closed Testing Procedures Are Admissible for Controlling False Discovery Proportions](https://doi.org/10.1214/20-AOS1999) - Goeman, Hemerik, and Solari (2021, *The Annals of Statistics*). Establishes the central role of closed testing in admissible simultaneous FDP inference.
- [Simultaneous False Discovery Proportion Bounds via Knockoffs and Closed Testing](https://doi.org/10.1093/jrsssb/qkae012) - Li, Maathuis, and Goeman (2024, *Journal of the Royal Statistical Society B*). Combines knockoffs with closed testing to bound FDP across adaptively selected sets.

## Discrete Tests and Conservative P-Values

- [A Modified Bonferroni Method for Discrete Data](https://doi.org/10.2307/2531456) - Tarone (1990, *Biometrics*). Exploits attainable significance levels to avoid spending error budget on hypotheses that cannot be rejected.
- [A Modified False Discovery Rate Multiple-Comparisons Procedure for Discrete Data, Applied to Human Immunodeficiency Virus Genetics](https://doi.org/10.1111/j.1467-9876.2005.00475.x) - Gilbert (2005, *Journal of the Royal Statistical Society C*). Adapts false discovery procedures to the discreteness of exact tests.
- [New FDR Bounds for Discrete and Heterogeneous Tests](https://doi.org/10.1214/18-EJS1441) - Döhler, Durand, and Roquain (2018, *Electronic Journal of Statistics*). Uses heterogeneous discrete null distributions to sharpen FDR procedures.
- [Multiple Testing When Many P-values Are Uniformly Conservative, with Application to Testing Qualitative Interaction in Educational Interventions](https://doi.org/10.1080/01621459.2018.1497499) - Zhao, Small, and Su (2019, *Journal of the American Statistical Association*). Conditional testing gains power when null p-values satisfy a uniform conservativeness property.

## Replicability and Directional Errors

An effect present in at least one study, an effect replicated in several studies, and a correctly inferred sign are distinct claims.

- [Screening for Partial Conjunction Hypotheses](https://doi.org/10.1111/j.1541-0420.2007.00984.x) - Benjamini and Heller (2008, *Biometrics*). Tests whether a signal is present in a specified minimum number of studies.
- [Discovering Findings That Replicate from a Primary Study of High Dimension to a Follow-Up Study](https://doi.org/10.1080/01621459.2013.829002) - Bogomolov and Heller (2013, *Journal of the American Statistical Association*). Controls errors in replicability claims after selecting features for follow-up.
- [Deciding Whether Follow-up Studies Have Replicated Findings in a Preliminary Large-Scale Omics Study](https://doi.org/10.1073/pnas.1314814111) - Heller, Bogomolov, and Benjamini (2014, *Proceedings of the National Academy of Sciences*). Develops r-values for quantifying evidence of replication.
- [Assessing Replicability of Findings across Two Studies of Multiple Features](https://doi.org/10.1093/biomet/asy029) - Bogomolov and Heller (2018, *Biometrika*). Replicability analysis when two studies screen overlapping features.
- [Detecting Multiple Replicating Signals Using Adaptive Filtering Procedures](https://doi.org/10.1214/21-AOS2139) - Wang et al. (2022, *The Annals of Statistics*). AdaFilter improves simultaneous partial-conjunction testing through adaptive filtering, with FWER and FDR procedures under the stated cross-study independence conditions.
- [Adaptive Procedures for Directional False Discovery Rate Control](https://doi.org/10.1214/24-EJS2213) - Leung and Tran (2024, *Electronic Journal of Statistics*). Adaptive methods that count incorrect effect directions among their errors.

## Variable Selection and Knockoffs

Start with the original knockoff paper. Fixed-X and model-X methods make different assumptions; model-X validity depends on the construction of suitable feature-distribution controls.

- [Panning for Gold: Model-X Knockoffs for High Dimensional Controlled Variable Selection](https://doi.org/10.1111/rssb.12265) - Candès, Fan, Janson, and Lv (2018, *Journal of the Royal Statistical Society B*). Extends knockoffs beyond fixed-design linear models to high-dimensional conditional variable selection.
- [Gene Hunting with Hidden Markov Model Knockoffs](https://doi.org/10.1093/biomet/asy033) - Sesia, Sabatti, and Candès (2019, *Biometrika*). Builds model-X knockoffs for genetic data using hidden Markov models.
- [False Discovery Rate Control via Debiased Lasso](https://doi.org/10.1214/19-EJS1554) - Javanmard and Javadi (2019, *Electronic Journal of Statistics*). Uses debiased regression estimates for asymptotic directional FDR control under sparsity and design conditions.
- [Robust Inference with Knockoffs](https://doi.org/10.1214/19-AOS1852) - Barber, Candès, and Samworth (2020, *The Annals of Statistics*). Quantifies how feature-distribution misspecification affects FDR control.
- [Metropolized Knockoff Sampling](https://doi.org/10.1080/01621459.2020.1729163) - Bates, Candès, Janson, and Wang (2021, *Journal of the American Statistical Association*). General knockoff sampling framework for complex feature distributions.
- [Powerful Knockoffs via Minimizing Reconstructability](https://doi.org/10.1214/21-AOS2104) - Spector and Janson (2022, *The Annals of Statistics*). Designs more powerful knockoffs by reducing reconstruction of original features from their controls.
- [False Discovery Rate Control via Data Splitting](https://doi.org/10.1080/01621459.2022.2060113) - Dai, Lin, Xing, and Liu (2023, *Journal of the American Statistical Association*). Mirror-statistic approach to variable selection using data splitting, with asymptotic guarantees under specified conditions.
- [Derandomised Knockoffs: Leveraging E-values for False Discovery Rate Control](https://doi.org/10.1093/jrsssb/qkad085) - Ren and Barber (2024, *Journal of the Royal Statistical Society B*). Aggregates repeated knockoff runs through e-values while retaining FDR control.

## Online Multiple Testing

Online testing allocates error across hypotheses arriving over time. Sequential monitoring allocates error across repeated looks within an experiment. Applying an online procedure does not by itself make an ordinary fixed-sample p-value safe to monitor continuously.

### Alpha Investing and Adaptive FDR

- [Generalized Alpha-Investing: Definitions, Optimality Results and Application to Public Databases](https://doi.org/10.1111/rssb.12048) - Aharoni and Rosset (2014, *Journal of the Royal Statistical Society B*). Generalizes alpha-investing rules and their marginal false discovery guarantees.
- [Online Control of the False Discovery Rate with Decaying Memory](https://proceedings.neurips.cc/paper_files/paper/2017/hash/7f018eb7b301a66658931cb8a93fd6e8-Abstract.html) - Ramdas, Yang, Wainwright, and Jordan (2017, *NeurIPS*). Introduces GAI++ improvements, including LORD++, and a separate decaying-memory error criterion.
- [Online Rules for Control of False Discovery Rate and False Discovery Exceedance](https://doi.org/10.1214/17-AOS1559) - Javanmard and Montanari (2018, *The Annals of Statistics*). Establishes online FDR and FDX guarantees for generalized alpha-investing procedures, including LORD variants.
- [SAFFRON: An Adaptive Algorithm for Online Control of the False Discovery Rate](https://proceedings.mlr.press/v80/ramdas18a.html) - Ramdas, Zrnic, Wainwright, and Jordan (2018, *ICML*). Adapts to the unknown null proportion using candidate p-values and an estimated false discovery budget.
- [ADDIS: An Adaptive Discarding Algorithm for Online FDR Control with Conservative Nulls](https://proceedings.neurips.cc/paper_files/paper/2019/hash/1d6408264d31d453d556c60fe7d0459e-Abstract.html) - Tian and Ramdas (2019, *NeurIPS*). Combines adaptation to null prevalence with discarding of conservative null p-values under the stated assumptions.
- [Contextual Online False Discovery Rate Control](https://proceedings.mlr.press/v108/chen20b.html) - Chen and Kasiviswanathan (2020, *AISTATS*). Learns how contextual features inform online rejection thresholds.
- [Structure–Adaptive Sequential Testing for Online False Discovery Rate Control](https://doi.org/10.1080/01621459.2021.1955688) - Gang, Sun, and Wang (2023, *Journal of the American Statistical Association*). Adapts sequential testing to evolving structure and heterogeneous signals.
- [Feedback-Enhanced Online Multiple Testing with Applications to Conformal Selection](https://www.jmlr.org/papers/v27/25-2123.html) - Lu et al. (2026, *Journal of Machine Learning Research*). Uses revealed hypothesis outcomes to improve subsequent decisions; distinguishes FDR and marginal FDR guarantees across feedback settings.

### Batches, Asynchrony, and Decision Deadlines

- [The Power of Batching in Multiple Hypothesis Testing](https://proceedings.mlr.press/v108/zrnic20a.html) - Zrnic, Jiang, Ramdas, and Jordan (2020, *AISTATS*). Batch-BH and Batch-Storey-BH interpolate between offline testing and an ongoing stream of hypothesis batches.
- [Asynchronous Online Testing of Multiple Hypotheses](https://www.jmlr.org/papers/v22/19-910.html) - Zrnic, Ramdas, and Jordan (2021, *Journal of Machine Learning Research*). Conflict sets handle overlapping experiments and local dependence; the error guarantee depends on the particular rule and assumptions.
- [Online Control of the False Discovery Rate under Decision Deadlines](https://proceedings.mlr.press/v151/fisher22a.html) - Fisher (2022, *AISTATS*). TOAD permits provisional decisions that can be updated until a predetermined deadline.
- [Online False Discovery Rate Control for LORD++ and SAFFRON under Positive, Local Dependence](https://doi.org/10.1002/bimj.202300177) - Fisher (2024, *Biometrical Journal*). Establishes guarantees under positive local dependence, including relevant batch-testing settings.

### Online FWER, FDX, and Confidence Statements

- [Online Control of the False Coverage Rate and False Sign Rate](https://proceedings.mlr.press/v119/weinstein20a.html) - Weinstein and Ramdas (2020, *ICML*). Constructs online selective confidence intervals and sign classifications with suitable error control.
- [Online Control of the Familywise Error Rate](https://doi.org/10.1177/0962280220983381) - Tian and Ramdas (2021, *Statistical Methods in Medical Research*). Develops online Šidák, fallback, and ADDIS-spending procedures for FWER control.
- [Dynamic Algorithms for Online Multiple Testing](https://proceedings.mlr.press/v145/xu22a.html) - Xu and Ramdas (2022, *Mathematical and Scientific Machine Learning*). SupLORD controls FDX and FDR at stopping times, with explicit conditions on when protection begins.
- [The Online Closure Principle](https://doi.org/10.1214/24-AOS2370) - Fischer, Bofill Roig, and Brannath (2024, *The Annals of Statistics*). Extends closed testing to online FWER procedures.
- [ADDIS-Graphs for Online Error Control with Application to Platform Trials](https://doi.org/10.1002/bimj.70075) - Fischer, Bofill Roig, and Brannath (2025, *Biometrical Journal*). Graphical online alpha allocation combines ADDIS spending with hypothesis priorities and local dependence.

## Sequential Testing and Adaptive Sampling

These papers repeatedly sample experiments within a family and may decide when to stop or where to collect the next observation. This differs from allocating levels to an incoming stream of completed tests. Type II error control concerns missed signals; FDR and FWER concern false rejections.

- [Sequential Tests of Multiple Hypotheses Controlling Type I and II Familywise Error Rates](https://doi.org/10.1016/j.jspi.2014.05.010) - Bartroff and Song (2014, *Journal of Statistical Planning and Inference*). Sequential Holm procedures jointly control familywise false rejections and false acceptances without requiring independence between data streams.
- [A Bandit Approach to Sequential Experimental Design with False Discovery Control](https://proceedings.neurips.cc/paper_files/paper/2018/hash/82cadb0649a3af4968404c9f6031b233-Abstract.html) - Jamieson and Jain (2018, *NeurIPS*). Allocates samples adaptively across candidate signals, studying error-control guarantees and sample complexity in a bandit setting.
- [Sequential Multiple Testing with Generalized Error Control: An Asymptotic Optimality Theory](https://doi.org/10.1214/18-AOS1737) - Song and Fellouris (2019, *The Annals of Statistics*). Develops efficient sequential procedures for generalized false-positive and false-negative criteria under independent streams as target error probabilities vanish.
- [A Unified Framework for Bandit Multiple Testing](https://proceedings.neurips.cc/paper_files/paper/2021/hash/8c460674cd61bf189e62b4da4bd9d7c1-Abstract.html) - Xu, Wang, and Ramdas (2021, *NeurIPS*). Uses valid e-processes to separate adaptive sampling from FDR-controlled decisions at arbitrary stopping times, including dependent-arm settings.
- [Asymptotically Optimal Sequential Multiple Testing with Asynchronous Decisions](https://doi.org/10.3150/24-BEJ1727) - Xing and Fellouris (2025, *Bernoulli*). Allows different decision times for independently monitored streams and characterizes their asymptotic efficiency under several global error criteria.

## E-Values and Anytime-Valid Inference

An e-value is a nonnegative statistic with null expectation at most one. An e-process provides suitable time-uniform validity. A collection of e-values at one time is not automatically an e-process.

- [Test Martingales, Bayes Factors and P-values](https://doi.org/10.1214/10-STS347) - Shafer, Shen, Vereshchagin, and Vovk (2011, *Statistical Science*). Connects sequential evidence, test martingales, Bayes factors, and p-values.
- [Time-Uniform, Nonparametric, Nonasymptotic Confidence Sequences](https://doi.org/10.1214/20-AOS1991) - Howard, Ramdas, McAuliffe, and Sekhon (2021, *The Annals of Statistics*). Develops confidence sequences for continuous monitoring within experiments.
- [E-values: Calibration, Combination and Applications](https://doi.org/10.1214/20-AOS2020) - Vovk and Wang (2021, *The Annals of Statistics*). Establishes e-value calibration and combination rules and their statistical uses.
- [False Discovery Rate Control with E-values](https://doi.org/10.1111/rssb.12489) - Wang and Ramdas (2022, *Journal of the Royal Statistical Society B*). Introduces e-BH, which controls FDR under arbitrary dependence between valid e-values.
- [Game-Theoretic Statistics and Safe Anytime-Valid Inference](https://doi.org/10.1214/23-STS894) - Ramdas, Grünwald, Vovk, and Shafer (2023, *Statistical Science*). Comprehensive review of safe testing, optional stopping, e-values, and e-processes.
- [Safe Testing](https://doi.org/10.1093/jrsssb/qkae011) - Grünwald, de Heide, and Koolen (2024, *Journal of the Royal Statistical Society B*). Develops safe testing through e-values and growth-rate optimality.
- [E-values as Unnormalized Weights in Multiple Testing](https://doi.org/10.1093/biomet/asad057) - Ignatiadis, Wang, and Ramdas (2024, *Biometrika*). Uses external e-values as weights to improve p-value-based testing under the required independence conditions.
- [Online Multiple Testing with E-values](https://proceedings.mlr.press/v238/xu24a.html) - Xu and Ramdas (2024, *AISTATS*). Introduces e-LOND for online FDR control under arbitrary dependence, with randomization and selective-inference extensions.
- [Post-Selection Inference for E-value Based Confidence Intervals](https://doi.org/10.1214/24-EJS2253) - Xu, Wang, and Ramdas (2024, *Electronic Journal of Statistics*). Constructs false coverage-rate guarantees after selection using e-value-based intervals.
- [Multiple Testing with Anytime-Valid Monte Carlo P-values](https://doi.org/10.1214/26-EJS2514) - Fischer, Barry, and Ramdas (2026, *Electronic Journal of Statistics*). Allows adaptive allocation and stopping of Monte Carlo computation while preserving multiple-testing validity.

## Applications

Selected methodological applications illustrate why the hypothesis family, resolution of a discovery, and dependence model matter. This section is not a catalogue of every field that uses adjusted p-values.

### Genomics and Proteomics

- [Significance Analysis of Microarrays Applied to the Ionizing Radiation Response](https://doi.org/10.1073/pnas.091062498) - Tusher, Tibshirani, and Chu (2001, *Proceedings of the National Academy of Sciences*). SAM combines gene-level statistics with permutation-based assessment of false discoveries.
- [Statistical Significance for Genomewide Studies](https://doi.org/10.1073/pnas.1530509100) - Storey and Tibshirani (2003, *Proceedings of the National Academy of Sciences*). Introduces q-value-based interpretation to genomewide significance analysis.
- [Target-Decoy Search Strategy for Increased Confidence in Large-Scale Protein Identifications by Mass Spectrometry](https://doi.org/10.1038/nmeth1019) - Elias and Gygi (2007, *Nature Methods*). Establishes target-decoy analysis for assessing false identifications in proteomics.
- [Independent Filtering Increases Detection Power for High-Throughput Experiments](https://doi.org/10.1073/pnas.0914005107) - Bourgon, Gentleman, and Huber (2010, *Proceedings of the National Academy of Sciences*). Shows when filtering before testing improves power without invalidating subsequent error control.

### Neuroimaging and Spatial Inference

- [Thresholding of Statistical Maps in Functional Neuroimaging Using the False Discovery Rate](https://doi.org/10.1006/nimg.2001.1037) - Genovese, Lazar, and Nichols (2002, *NeuroImage*). Influential application of FDR to voxelwise brain maps.
- [Controlling the Familywise Error Rate in Functional Neuroimaging: A Comparative Review](https://doi.org/10.1191/0962280203sm341ra) - Nichols and Hayasaka (2003, *Statistical Methods in Medical Research*). Compares random-field, permutation, and related familywise approaches.
- [False Discovery Rates for Spatial Signals](https://doi.org/10.1198/016214507000000941) - Benjamini and Heller (2007, *Journal of the American Statistical Association*). Uses spatial structure while distinguishing cluster-level and voxel-level discoveries.
- [Cluster Failure: Why fMRI Inferences for Spatial Extent Have Inflated False-Positive Rates](https://doi.org/10.1073/pnas.1602413113) - Eklund, Nichols, and Knutsson (2016, *Proceedings of the National Academy of Sciences*). Empirical evaluation showing the consequences of violated assumptions in cluster-level inference.
- [Influence of Multiple Hypothesis Testing on Reproducibility in Neuroimaging Research: A Simulation Study and Python-Based Software](https://doi.org/10.1016/j.jneumeth.2020.108654) - Puoliväli, Palva, and Palva (2020, *Journal of Neuroscience Methods*). Compares multiple-testing approaches in simulations and introduces the multipy research implementation.

### Anomaly Detection and Conformal Selection

- [Online False Discovery Rate Control for Anomaly Detection in Time Series](https://proceedings.neurips.cc/paper_files/paper/2021/hash/def130d0b67eb38b7a8f4e7121ed432c-Abstract.html) - Rebjock, Kurt, Januschowski, and Callot (2021, *NeurIPS*). Develops online anomaly-detection rules addressing rare signals and temporal dependence under the proposed error criteria.
- [Testing for Outliers with Conformal P-values](https://doi.org/10.1214/22-AOS2244) - Bates et al. (2023, *The Annals of Statistics*). Studies conformal p-values and multiple-testing guarantees for outlier detection.
- [Selection by Prediction with Conformal P-values](https://www.jmlr.org/papers/v24/22-1176.html) - Jin and Candès (2023, *Journal of Machine Learning Research*). Screens candidates for sufficiently large unobserved outcomes using conformal p-values and FDR control under exchangeability assumptions.
- [Adaptive Novelty Detection with False Discovery Rate Guarantee](https://doi.org/10.1214/23-AOS2338) - Marandon, Lei, Mary, and Roquain (2024, *The Annals of Statistics*). Combines adaptive scoring with novelty detection and a finite-sample FDR guarantee.

### Experiments and Clinical Trials

- [Multiple Hypothesis Testing in Experimental Economics](https://doi.org/10.1007/s10683-018-09597-5) - List, Shaikh, and Xu (2019, *Experimental Economics*). Designs multiplicity adjustments around experimental treatment comparisons and outcomes.
- [Always Valid Inference: Continuous Monitoring of A/B Tests](https://doi.org/10.1287/opre.2021.2135) - Johari, Koomen, Pekelis, and Walsh (2022, *Operations Research*). Develops continuously monitorable inference and examines its use in multiple testing.
- [Online Control of the False Discovery Rate in Group-Sequential Platform Trials](https://doi.org/10.1177/09622802221129051) - Zehetmayer, Posch, and Koenig (2022, *Statistical Methods in Medical Research*). Combines multiple treatment comparisons with interim analyses in platform trials.
- [Online Error Rate Control for Platform Trials](https://doi.org/10.1002/sim.9733) - Robertson et al. (2023, *Statistics in Medicine*). Compares online error-control strategies for trials with treatments entering over time.

## Authoritative Monographs

These are explicit exceptions to the research-paper policy: established scholarly reference books by foundational contributors to multiple comparisons, resampling, genomic testing, and empirical Bayes. A book's editorial publication is not represented as journal-article peer review. The [exception register](docs/publication-exceptions.json) records the rationale and supporting publications.

- [Multiple Comparison Procedures](https://doi.org/10.1002/9780470316672) - Hochberg and Tamhane (1987, *Wiley*). **Monograph.** Comprehensive theory of simultaneous tests and confidence intervals by leading developers of multiple-comparison procedures.
- [Resampling-Based Multiple Testing: Examples and Methods for P-value Adjustment](https://www.wiley.com/en-us/resampling-based-multiple-testing-examples-and-methods-for-p-value-adjustment-p-9780471557616) - Westfall and Young (1993, *Wiley*). **Monograph.** Foundational reference for resampling-adjusted p-values, dependence, and Westfall–Young procedures.
- [Multiple Testing Procedures with Applications to Genomics](https://doi.org/10.1007/978-0-387-49317-6) - Dudoit and van der Laan (2008, *Springer*). **Monograph.** Systematic treatment of multiple-testing error criteria, resampling, and genomic applications.
- [Large-Scale Inference: Empirical Bayes Methods for Estimation, Testing, and Prediction](https://doi.org/10.1017/CBO9780511761362) - Efron (2010, *Cambridge University Press*). **Monograph.** Connects empirical Bayes, local FDR, null estimation, and large-scale inference.

## Software

Official documentation and package registries are listed here for implementation. Follow the cited methods for assumptions and guarantees; a software package does not make an arbitrary analysis valid.

### R

- [stats: p.adjust](https://stat.ethz.ch/R-manual/R-patched/library/stats/html/p.adjust.html) - Base R implementations of Bonferroni, Holm, Hochberg, Hommel, BH, and BY from the classical literature.
- [multcomp](https://cran.r-project.org/package=multcomp) - Simultaneous tests and confidence intervals for model contrasts, based on [Hothorn, Bretz, and Westfall](https://doi.org/10.1002/bimj.200810425).
- [multtest](https://bioconductor.org/packages/multtest) - Resampling-based multiple testing, including maxT and minP approaches; see the [Dudoit–Shaffer–Boldrick review](https://doi.org/10.1214/ss/1056397487).
- [qvalue](https://bioconductor.org/packages/qvalue) - Q-value and null-proportion estimation following [Storey and Tibshirani](https://doi.org/10.1073/pnas.1530509100).
- [IHW](https://bioconductor.org/packages/IHW) - Independent hypothesis weighting with informative covariates, based on [Ignatiadis et al.](https://doi.org/10.1038/nmeth.3885).
- [adaptMT](https://cran.r-project.org/package=adaptMT) - AdaPT implementation for interactive multiple testing with side information, following [Lei and Fithian](https://doi.org/10.1111/rssb.12274).
- [ashr](https://cran.r-project.org/package=ashr) - Adaptive shrinkage, local false discovery rates, and local false sign rates following [Stephens](https://doi.org/10.1093/biostatistics/kxw041).
- [fdrtool](https://cran.r-project.org/package=fdrtool) - Empirical-null and local or tail-area FDR estimation, described by [Strimmer](https://doi.org/10.1093/bioinformatics/btn209).
- [hommel](https://cran.r-project.org/package=hommel) - Efficient Hommel adjustment and related simultaneous inference, based on [Meijer, Krebs, and Goeman](https://doi.org/10.1002/bimj.201700316).
- [cherry](https://cran.r-project.org/package=cherry) - Exploratory closed testing and simultaneous false-discovery bounds following [Goeman and Solari](https://doi.org/10.1214/11-STS356).
- [DiscreteFDR](https://cran.r-project.org/package=DiscreteFDR) - Discrete and heterogeneous-test FDR procedures based on [Döhler, Durand, and Roquain](https://doi.org/10.1214/18-EJS1441).
- [gMCP](https://cran.r-project.org/package=gMCP) - Graphical multiple-comparison procedures following [Bretz et al.](https://doi.org/10.1002/bimj.201000239).
- [knockoff](https://cran.r-project.org/package=knockoff) - Fixed-X and model-X knockoff implementations from the knockoff literature.
- [onlineFDR](https://bioconductor.org/packages/onlineFDR) - Online FDR and FWER procedures, including LORD, SAFFRON, ADDIS, asynchronous rules, and batch methods; introduced in [Robertson et al.](https://doi.org/10.1093/bioinformatics/btz191).

### Python

- [statsmodels: multipletests](https://www.statsmodels.org/stable/generated/statsmodels.stats.multitest.multipletests.html) - Classical FWER and FDR adjustments, including two-stage procedures; consult the API's method-specific assumptions.
- [SciPy: false_discovery_control](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.false_discovery_control.html) - BH and BY adjusted p-values, with the original papers cited in the documentation.
- [knockpy](https://amspector100.github.io/knockpy) - Knockoff generation and feature selection, including methods from [Spector and Janson](https://doi.org/10.1214/21-AOS2104).

### Julia

- [MultipleTesting.jl](https://github.com/juliangehring/MultipleTesting.jl) - P-value adjustment, combination, and null-proportion estimation with documented references to the implemented methods.

### Research Implementations

See [Historical and Paper-Specific Code](docs/RESEARCH_CODE.md) for original SAFFRON, ADDIS, Batch-BH, and multipy implementations. Reproducibility code may have inactive development or older dependencies.

## Related Lists

- [Awesome Statistics](https://github.com/erikgahner/awesome-statistics) - General statistical learning resources beyond multiple testing.
- [Awesome Bioinformatics Benchmarks](https://github.com/j-andrews7/awesome-bioinformatics-benchmarks) - Benchmark studies, including comparisons of false discovery procedures.
- [Awesome Conformal Prediction](https://github.com/valeman/awesome-conformal-prediction) - Broader coverage of conformal prediction and uncertainty quantification.

## Contributing

Read the [contribution guidelines](CONTRIBUTING.md) for publication requirements, annotations, exception criteria, and validation commands. The [maintenance guide](docs/MAINTENANCE.md) explains automated checks and the manual review they cannot replace.
