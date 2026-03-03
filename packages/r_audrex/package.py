# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAudrex(RPackage):
	"""Automatic Dynamic Regression using Extreme Gradient Boosting

	Dynamic regression for time series using Extreme Gradient Boosting with hyper-parameter tuning via Bayesian Optimization or Random Search.
	"""
	
	homepage = "https://rpubs.com/giancarlo_vercellino/audrex"
	cran = "audrex" 

	version("2.0.1", md5="5689ce83126121c1f80240fa9fe18d8f")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-rbayesianoptimization@1.2:", type=("build", "run"))
	depends_on("r-xgboost@1.4.1.1:", type=("build", "run"))
	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.5:", type=("build", "run"))
	depends_on("r-readr@2.1.2:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-lubridate@1.7.10:", type=("build", "run"))
	depends_on("r-narray@0.4.1.1:", type=("build", "run"))
	depends_on("r-fancova@0.6.1:", type=("build", "run"))
	depends_on("r-imputets@3.2:", type=("build", "run"))
	depends_on("r-scales@1.1.1:", type=("build", "run"))
	depends_on("r-tictoc@1.0.1:", type=("build", "run"))
	depends_on("r-modeest@2.4:", type=("build", "run"))
	depends_on("r-moments@0.14:", type=("build", "run"))
	depends_on("r-metrics@0.1.4:", type=("build", "run"))
