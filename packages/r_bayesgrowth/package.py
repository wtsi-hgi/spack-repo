# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesgrowth(RPackage):
	"""Estimate Fish Growth Using MCMC Analysis

	Estimate fish length-at-age models using MCMC analysis with 
    'rstan' models. This package allows a multimodel approach to growth fitting
    to be applied to length-at-age data and is supported by further analyses to 
    determine model selection and result presentation. The core methods of this 
    package are presented in Smart and Grammer (2021) "Modernising fish and 
    shark growth curves with Bayesian length-at-age models". PLOS ONE 16(2):
    e0246734 <doi:10.1371/journal.pone.0246734>.
	"""
	
	homepage = "https://github.com/jonathansmart/BayesGrowth"
	cran = "BayesGrowth" 

	version("1.0.0", md5="d58b61a788792d43daa3ea0cb9c30944")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-aquaticlifehistory", type=("build", "run"))
	depends_on("r-bayesplot", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-loo", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
	depends_on("r-rstan@2.18.1:", type=("build", "run"))
	depends_on("r-rstantools@2.3.1.1:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidybayes", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-stanheaders@2.18:", type=("build", "run"))
