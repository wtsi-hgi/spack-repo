# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUgomquantreg(RPackage):
	"""Quantile Regression Modeling for Unit-Gompertz Responses

	Unit-Gompertz density, cumulative distribution, quantile functions and random deviate
   	generation of the unit-Gompertz distribution. In addition, there are a function for fitting the 
   	Generalized Additive Models for Location, Scale and Shape.
	"""
	
	cran = "ugomquantreg" 

	version("1.0.0", md5="99dcfab6ed154084f87faff27a886d71")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-gamlss", type=("build", "run"))
	depends_on("r-gamlss-dist", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
