# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAgroreg(RPackage):
	"""Regression Analysis Linear and Nonlinear for Agriculture

	Linear and nonlinear regression analysis common in agricultural science articles (Archontoulis & Miguez (2015). <doi:10.2134/agronj2012.0506>). The package includes polynomial, exponential, gaussian, logistic, logarithmic, segmented, non-parametric models, among others. The functions return the model coefficients and their respective p values, coefficient of determination, root mean square error, AIC, BIC, as well as graphs with the equations automatically.
	"""
	
	homepage = "https://fisher.uel.br/AgroReg_shiny/"
	cran = "AgroReg" 

	version("1.2.10", md5="9087adbac21310dc8eb3b9cbc04773df")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-drc", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rcompanion", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-egg", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
