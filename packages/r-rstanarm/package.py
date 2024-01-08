# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
	
from spack.package import *
	
			
class RRstanarm(RPackage):
	"""Bayesian Applied Regression Modeling via Stan

	Estimates previously compiled regression models using the 'rstan'
    package, which provides the R interface to the Stan C++ library for Bayesian
    estimation. Users specify models via the customary R syntax with a formula and
    data.frame plus some additional arguments for priors.
	"""
	
	homepage = "https://mc-stan.org/rstanarm/"
	cran = "rstanarm" 

	version("2.26.1", md5="8505a33ae9ff139e9f0b3d5b8cc6ee7e")

	depends_on("r@3.4.0:", type=("build", "run"))
	depends_on("r-rcpp@0.12.0:", type=("build", "run"))
	depends_on("r-bayesplot@1.7.0:", type=("build", "run"))
	depends_on("r-ggplot2@2.2.1:", type=("build", "run"))
	depends_on("r-lme4@1.1-8:", type=("build", "run"))
	depends_on("r-loo@2.1.0:", type=("build", "run"))
	depends_on("r-matrix@1.2-13:", type=("build", "run"))
	depends_on("r-nlme@3.1-124:", type=("build", "run"))
	depends_on("r-posterior", type=("build", "run"))
	depends_on("r-rstan@2.26.1:", type=("build", "run"))
	depends_on("r-rstantools@2.1.0:", type=("build", "run"))
	depends_on("r-shinystan@2.3.0:", type=("build", "run"))
	depends_on("r-survival@2.40.1:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
	depends_on("r-stanheaders@2.21.0:", type=("build", "run"))
	depends_on("r-rstan@2.21.1:", type=("build", "run"))
	depends_on("r-bh@1.72.0-2:", type=("build", "run"))
	depends_on("r-rcpp@0.12.0:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3.0:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
