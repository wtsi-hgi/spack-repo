# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDisbayes(RPackage):
	"""Bayesian Multi-State Modelling of Chronic Disease Burden Data

	Estimation of incidence and case fatality for a chronic disease, given partial information, using a multi-state model. Given data on age-specific mortality and either incidence or prevalence, Bayesian inference is used to estimate the posterior distributions of incidence, case fatality, and functions of these such as prevalence.  The methods are described in Jackson et al. (2023) <doi:10.1093/jrsssa/qnac015>.
	"""
	
	homepage = "https://chjackson.github.io/disbayes/"
	cran = "disbayes" 

	version("1.1.0", md5="7eea9037cf2ede66adf8c802c32912f0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rstan@2.26:", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-shelf", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-loo", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-stanheaders@2.26:", type=("build", "run"))
	depends_on("r-rstantools", type=("build", "link", "run"))
