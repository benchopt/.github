# Benchmarks gallery

To reproduce/modify a benchmark,
    
1. clone the benchmark repository and ``cd`` into it,

```shell
$ git clone https://github.com/benchopt/{REPOSITORY_NAME}.git
$ cd {REPOSITORY_NAME}
```

2. install ``benchopt`` to use its API/CLI,

```shell
$ pip install -U benchopt
```
    
3. run the following command to reproduce the benchmark,

```shell
$ benchopt run .
```

Et Voilà! Refer to [``Benchopt`` API](https://benchopt.github.io/cli.html#benchopt-run) 
to explore the different options for running a benchmark.


## Available benchmarks

- [Convolutional sparse coding](https://api.github.com/repos/benchopt/benchmark_csc) ![Test status](https://github.com/benchopt/benchmark_csc/actions/workflows/main.yml/badge.svg)
- [The elastic net problem](https://api.github.com/repos/benchopt/benchmark_elastic_net) ![Test status](https://github.com/benchopt/benchmark_elastic_net/actions/workflows/main.yml/badge.svg)
- [Glm model](https://api.github.com/repos/benchopt/benchmark_glm) ![Test status](https://github.com/benchopt/benchmark_glm/actions/workflows/main.yml/badge.svg)
- [No description.](https://api.github.com/repos/benchopt/benchmark_huber_l2) ![Test status](https://github.com/benchopt/benchmark_huber_l2/actions/workflows/main.yml/badge.svg)
- [Approximate joint diagonalization (ajd)](https://api.github.com/repos/benchopt/benchmark_jointdiag) ![Test status](https://github.com/benchopt/benchmark_jointdiag/actions/workflows/main.yml/badge.svg)
- [Lasso](https://api.github.com/repos/benchopt/benchmark_lasso) ![Test status](https://github.com/benchopt/benchmark_lasso/actions/workflows/main.yml/badge.svg)
- [Linear ica](https://api.github.com/repos/benchopt/benchmark_linear_ica) ![Test status](https://github.com/benchopt/benchmark_linear_ica/actions/workflows/main.yml/badge.svg)
- [Svm  binary classification](https://api.github.com/repos/benchopt/benchmark_linear_svm_binary_classif_no_intercept) ![Test status](https://github.com/benchopt/benchmark_linear_svm_binary_classif_no_intercept/actions/workflows/main.yml/badge.svg)
- [Sparse logistic regression](https://api.github.com/repos/benchopt/benchmark_logreg_l1) ![Test status](https://github.com/benchopt/benchmark_logreg_l1/actions/workflows/main.yml/badge.svg)
- [L2-regularized logistic regression](https://api.github.com/repos/benchopt/benchmark_logreg_l2) ![Test status](https://github.com/benchopt/benchmark_logreg_l2/actions/workflows/main.yml/badge.svg)
- [No description.](https://api.github.com/repos/benchopt/benchmark_mcp) ![Test status](https://github.com/benchopt/benchmark_mcp/actions/workflows/main.yml/badge.svg)
- [Non-negative least square](https://api.github.com/repos/benchopt/benchmark_nnls) ![Test status](https://github.com/benchopt/benchmark_nnls/actions/workflows/main.yml/badge.svg)
- [Ordinary least square](https://api.github.com/repos/benchopt/benchmark_ols) ![Test status](https://github.com/benchopt/benchmark_ols/actions/workflows/main.yml/badge.svg)
- [Quantile regression](https://api.github.com/repos/benchopt/benchmark_quantile_regression) ![Test status](https://github.com/benchopt/benchmark_quantile_regression/actions/workflows/main.yml/badge.svg)
- [Resnet fitting on a classification task](https://api.github.com/repos/benchopt/benchmark_resnet_classif) ![Test status](https://github.com/benchopt/benchmark_resnet_classif/actions/workflows/main.yml/badge.svg)
- [No description.](https://api.github.com/repos/benchopt/benchmark_ridge) ![Test status](https://github.com/benchopt/benchmark_ridge/actions/workflows/main.yml/badge.svg)
- [Tv denoising in 1d](https://api.github.com/repos/benchopt/benchmark_tv_1d) ![Test status](https://github.com/benchopt/benchmark_tv_1d/actions/workflows/main.yml/badge.svg)
- [Tv-regularized problem in 2d](https://api.github.com/repos/benchopt/benchmark_tv_2d) ![Test status](https://github.com/benchopt/benchmark_tv_2d/actions/workflows/main.yml/badge.svg)
