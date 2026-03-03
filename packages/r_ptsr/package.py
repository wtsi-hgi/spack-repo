# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPtsr(RPackage):
	"""Positive Time Series Regression

	A collection of functions to simulate, estimate and forecast a wide range of regression based dynamic models for positive time series. 
	This package implements the results presented in Prass, T.S.; Carlos, J.H.; Taufemback, C.G. and Pumi, G. (2022). "Positive Time Series Regression" <arXiv:2201.03667>.
	"""
	
	cran = "PTSR" 

	version("0.1.2", md5="86a801d03acaec217460eaee73df787d")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-extradistr", type=("build", "run"))
	depends_on("r-suppdists", type=("build", "run"))
	depends_on("r-actuar", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
