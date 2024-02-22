# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrmreg(RPackage):
	"""Cellwise Robust M-Regression and SPADIMO

	Method for fitting a cellwise robust linear M-regression model (CRM, Filzmoser et al. (2020) <DOI:10.1016/j.csda.2020.106944>) that yields both a map of cellwise outliers consistent with the linear model, and a vector of regression coefficients that is robust against vertical outliers and leverage points. As a by-product, the method yields an imputed data set that contains estimates of what the values in cellwise outliers would need to amount to if they had fit the model. The package also provides diagnostic tools for analyzing casewise and cellwise outliers using sparse directions of maximal outlyingness (SPADIMO, Debruyne et al. (2019) <DOI:10.1007/s11222-018-9831-5>).
	"""
	
	cran = "crmReg" 

	version("1.0.2", md5="fca18c27fcb5c1fd3f6344d2ef35dd44")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-pcapp", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-rrcov", type=("build", "run"))
