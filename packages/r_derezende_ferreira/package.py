# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDerezendeFerreira(RPackage):
	"""Zero Coupon Yield Curve Modelling

	Modeling the zero coupon yield curve using the dynamic De Rezende and
             Ferreira (2011) <doi:10.1002/for.1256> five factor model with variable
             or fixed decaying parameters. For explanatory purposes, the package also
             includes various short datasets of interest rates for the BRICS countries. 
	"""
	
	cran = "DeRezende.Ferreira" 

	version("0.1.0", md5="627d91e430b1d712f675ec52373b303e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
