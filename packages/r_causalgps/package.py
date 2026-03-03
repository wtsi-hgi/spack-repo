# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCausalgps(RPackage):
	"""Matching on Generalized Propensity Scores with Continuous
Exposures

	Provides a framework for estimating causal effects of a continuous 
    exposure using observational data, and implementing matching and weighting 
    on the generalized propensity score.
    Wu, X., Mealli, F., Kioumourtzoglou, M.A., Dominici, F. and Braun, D., 2022. 
    Matching on generalized propensity scores with continuous exposures. Journal 
    of the American Statistical Association, pp.1-29.
	"""
	
	homepage = "https://github.com/NSAPH-Software/CausalGPS"
	cran = "CausalGPS" 

	version("0.4.1", md5="b9eb098b3ea52dd9495d4dea8c726f38")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-superlearner", type=("build", "run"))
	depends_on("r-xgboost", type=("build", "run"))
	depends_on("r-gam", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-polycor", type=("build", "run"))
	depends_on("r-wcorr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-logger", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-gnm", type=("build", "run"))
	depends_on("r-locpol", type=("build", "run"))
	depends_on("r-ecume", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
