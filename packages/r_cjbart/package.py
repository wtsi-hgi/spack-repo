# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCjbart(RPackage):
	"""Heterogeneous Effects Analysis of Conjoint Experiments

	A tool for analyzing conjoint experiments using Bayesian Additive Regression Trees ('BART'), a machine learning method developed by Chipman, George and McCulloch (2010) <doi:10.1214/09-AOAS285>. This tool focuses specifically on estimating, identifying, and visualizing the heterogeneity within marginal component effects, at the observation- and individual-level. It uses a variable importance measure ('VIMP') with delete-d jackknife variance estimation, following Ishwaran and Lu (2019) <doi:10.1002/sim.7803>, to obtain bias-corrected estimates of which variables drive heterogeneity in the predicted individual-level effects.
	"""
	
	homepage = "https://github.com/tsrobinson/cjbart"
	cran = "cjbart" 

	version("0.3.2", md5="5d0ee2943c1170243ac88cb447ae3162")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-bart", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-randomforestsrc@3.2.2:", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
