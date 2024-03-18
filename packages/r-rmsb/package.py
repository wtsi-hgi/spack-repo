# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmsb(RPackage):
	"""Bayesian Regression Modeling Strategies

	A Bayesian companion to the 'rms' package, 'rmsb' provides Bayesian model fitting, post-fit estimation, and graphics.  It implements Bayesian regression models whose fit objects can be processed by 'rms' functions such as 'contrast()', 'summary()', 'Predict()', 'nomogram()', and 'latex()'.  The fitting function currently implemented in the package is 'blrm()' for Bayesian logistic binary and ordinal regression with optional clustering, censoring, and departures from the proportional odds assumption using the partial proportional odds model of Peterson and Harrell (1990) <https://www.jstor.org/stable/2347760>.
	"""
	
	homepage = "https://hbiostat.org/R/rmsb/"
	cran = "rmsb" 

	version("1.1-0", md5="e8a881a79cc3c393a56bad1f7f202560")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rms@6.8.0:", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rstan@2.18.1:", type=("build", "run"))
	depends_on("r-hmisc@4.3.0:", type=("build", "run"))
	depends_on("r-survival@3.1.12:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-loo", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
	depends_on("r-stanheaders@2.18:", type=("build", "run"))
	depends_on("r-rstantools", type=("build", "link", "run"))
