# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAgd(RPackage):
	"""Analysis of Growth Data

	Tools for the analysis of growth data: to extract an 
    LMS table from a gamlss object, to calculate the standard 
    deviation scores and its inverse, and to superpose two wormplots 
    from different models. The package contains a some varieties of 
    reference tables, especially for The Netherlands.
	"""
	
	homepage = "https://github.com/stefvanbuuren/AGD"
	cran = "AGD" 

	version("0.39", md5="a77fa346d88016076918b18dd39f0d6d")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-gamlss", type=("build", "run"))
	depends_on("r-gamlss-dist", type=("build", "run"))
