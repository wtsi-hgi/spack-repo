# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSure(RPackage):
	"""Surrogate Residuals for Ordinal and General Regression Models

	An implementation of the surrogate approach to residuals and 
  diagnostics for ordinal and general regression models; for details, see Liu 
  and Zhang (2017) <doi:10.1080/01621459.2017.1292915>. These residuals can be 
  used to construct standard residual plots for model diagnostics (e.g., 
  residual-vs-fitted value plots, residual-vs-covariate plots, Q-Q plots, etc.). 
  The package also provides an 'autoplot' function for producing standard 
  diagnostic plots using 'ggplot2' graphics. The package currently supports 
  cumulative link models from packages 'MASS', 'ordinal', 'rms', and 'VGAM'. 
  Support for binary regression models using the standard 'glm' function is also 
  available.
	"""
	
	homepage = "https://github.com/AFIT-R/sure"
	cran = "sure" 

	version("0.2.0", md5="b4cb1924972fa23db35851275cd267d9")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-ggplot2@2.2.1:", type=("build", "run"))
	depends_on("r-goftest", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
