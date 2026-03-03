# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCodaredistlm(RPackage):
	"""Compositional Data Linear Models with Composition Redistribution

	Provided data containing an outcome variable, compositional variables and additional covariates (optional); linearly regress the outcome variable on an isometric log ratio (ilr) transformation of the linearly dependent compositional variables. The package provides predictions (with confidence intervals) in the change (delta) in the outcome/response variable based on the multiple linear regression model and evenly spaced reallocations of the compositional values. The compositional data analysis approach implemented is outlined in Dumuid et al. (2017a) <doi:10.1177/0962280217710835> and Dumuid et al. (2017b) <doi:10.1177/0962280217737805>.
	"""
	
	homepage = "https://github.com/tystan/codaredistlm"
	cran = "codaredistlm" 

	version("0.1.0", md5="1db3af52a69e2f69125c4145822d8482")

	depends_on("r-compositions", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
