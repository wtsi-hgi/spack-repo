# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFixedincome(RPackage):
	"""Fixed Income Models, Calculations, Data Structures and
Instruments

	Fixed income mathematics made easy. A rich set of functions 
    that helps with calculations of interest rates and fixed income.
    It has objects that abstract interest rates, compounding factors, day count rules,
    forward rates and term structure of interest rates.
    Many interpolation methods and parametric curve models commonly used by practitioners
    are implemented.
	"""
	
	homepage = "https://github.com/wilsonfreitas/R-fixedincome"
	cran = "fixedincome" 

	version("0.0.5", md5="eceab53c03407e3cbcca11d4fc7b54f0")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-bizdays@1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
