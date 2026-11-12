# Research Code

Historical and paper-specific implementations are useful for reproducing published experiments. They are kept separate from the main software recommendations because their dependencies or development activity may be dated. These repositories were not executed as part of the bibliography audit.

- [SAFFRONcode](https://github.com/tijana-zrnic/SAFFRONcode) - Original experiment code for Ramdas et al.'s [SAFFRON paper](https://proceedings.mlr.press/v80/ramdas18a.html), published at ICML 2018. This is the SAFFRON repository; the ADDIS repository is a different project.
- [ADDIS](https://github.com/JINJINT/ADDIS) - Author implementation and figure-reproduction scripts for Tian and Ramdas's [ADDIS paper](https://proceedings.neurips.cc/paper_files/paper/2019/hash/1d6408264d31d453d556c60fe7d0459e-Abstract.html), published at NeurIPS 2019.
- [BatchBH](https://github.com/jiangdaniel/BatchBH) - Experiment code for Zrnic et al.'s [The Power of Batching in Multiple Hypothesis Testing](https://proceedings.mlr.press/v108/zrnic20a.html), published at AISTATS 2020. Includes Batch-BH and Batch-Storey-BH experiments; the repository documents its original Python environment.
- [multipy](https://github.com/puolival/multipy) - Python research implementation accompanying Puoliväli, Palva, and Palva's [2020 neuroimaging simulation study](https://doi.org/10.1016/j.jneumeth.2020.108654). Useful for reproducing the comparison, but check compatibility before adopting it in a new workflow.

For documented package implementations of online and batched procedures, start with [onlineFDR](https://bioconductor.org/packages/onlineFDR). For common Python p-value adjustments, see the [main software section](../README.md#python).
