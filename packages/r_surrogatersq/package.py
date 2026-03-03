# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurrogatersq(RPackage):
	"""Goodness-of-Fit Analysis for Categorical Data using the
Surrogate R-Squared

	To assess and compare the models' goodness of fit, R-squared is one of the most 
              popular measures. For categorical data analysis, however, no universally adopted 
              R-squared measure can resemble the ordinary least square (OLS) R-squared for 
              linear models with continuous data. This package implement the surrogate R-squared
              measure for categorical data analysis, which is proposed in the study of Dungang Liu,
              Xiaorui Zhu, Brandon Greenwell, and Zewei Lin (2022) <doi:10.1111/bmsp.12289>. It
              can generate a point or interval measure of the surrogate R-squared. It can also 
              provide a ranking measure of the percentage contribution of each variable to the 
              overall surrogate R-squared. This ranking assessment allows one to check the 
              importance of each variable in terms of their explained variance. This package can
              be jointly used with other existing R packages for variable selection and model 
              diagnostics in the model-building process. 
	"""
	
	homepage = "https://xiaorui.site/SurrogateRsq/"
	cran = "SurrogateRsq" 

	version("0.2.1", md5="ad6be423115c0930ca4f2e7c84c39716")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass@7.3.54:", type=("build", "run"))
	depends_on("r-passo@0.1.10:", type=("build", "run"))
	depends_on("r-progress@1.2:", type=("build", "run"))
	depends_on("r-scales@1.1.1:", type=("build", "run"))
