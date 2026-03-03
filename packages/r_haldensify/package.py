# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHaldensify(RPackage):
	"""Highly Adaptive Lasso Conditional Density Estimation

	An algorithm for flexible conditional density estimation based on
    application of pooled hazard regression to an artificial repeated measures
    dataset constructed by discretizing the support of the outcome variable. To
    facilitate non/semi-parametric estimation of the conditional density, the
    highly adaptive lasso, a nonparametric regression function shown to reliably
    estimate a large class of functions at a fast convergence rate, is utilized.
    The pooled hazards data augmentation formulation implemented was first
    described by Díaz and van der Laan (2011) <doi:10.2202/1557-4679.1356>. To
    complement the conditional density estimation utilities, tools for efficient
    nonparametric inverse probability weighted (IPW) estimation of the causal
    effects of stochastic shift interventions (modified treatment policies),
    directly utilizing the density estimation technique for construction of the
    generalized propensity score, are provided. These IPW estimators utilize
    undersmoothing (sieve estimation) of the conditional density estimators in
    order to achieve the non/semi-parametric efficiency bound.
	"""
	
	homepage = "https://github.com/nhejazi/haldensify"
	cran = "haldensify" 

	version("0.2.3", md5="5bfafd8ce5b427011936fdd03e129740")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-hal9001@0.4.1:", type=("build", "run"))
	depends_on("r-origami@1.0.3:", type=("build", "run"))
	depends_on("r-rsample", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
