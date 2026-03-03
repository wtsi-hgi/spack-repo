# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSglg(RPackage):
	"""Fitting Semi-Parametric Generalized log-Gamma Regression Models

	Set of tools to fit a linear multiple or semi-parametric regression
    models with the possibility of non-informative random right-censoring. 
    Under this setup, the localization parameter of the response variable distribution is modeled by using linear multiple regression
    or semi-parametric functions, whose non-parametric components may be approximated
    by natural cubic spline or P-splines. The supported distribution for the model error is a generalized log-gamma distribution which includes
    the generalized extreme value and standard normal distributions as important special cases. Inference is based on penalized likelihood and bootstrap methods.   
    Also, some numerical and graphical devices for diagnostic of the fitted models are offered. 
	"""
	
	cran = "sglg" 

	version("0.2.2", md5="6691f66dc9097b574f0d95d2c0d5b252")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-adequacymodel", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-moments", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-plot3d", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-teachingsampling", type=("build", "run"))
