# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REmbayes(RPackage):
	"""Robust Bayesian Variable Selection via Expectation-Maximization

	Variable selection methods have been extensively developed for analyzing high-dimensional omics data within both the frequentist and Bayesian frameworks. This package implemented the spike-and-slab quantile LASSO which has been developed along the line of Bayesian hierarchical model but deeply rooted in the frequentist regularization methods by utilizing the Expectation–Maximization (EM) algorithm. Therefore, the proposed method borrows strength from both the frequentist and Bayesian frameworks while overcoming their respective limitations. The spike-and-slab quantile LASSO can handle data irregularity in terms of skewness and outliers in the disease trait, compared to its nonrobust alternative, the spike-and-slab LASSO, which has also been implemented in the package. The core module of this package is developed in 'C++'.
	"""
	
	cran = "emBayes" 

	version("0.1.4", md5="8c9af9d9d0ec5c662e897e7736a74314")
	version("0.1.5", md5="f092a98d8b2ebb2792daf95fd5015e40")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
