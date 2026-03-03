# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGuerry(RPackage):
	"""Maps, Data and Methods Related to Guerry (1833) "Moral
Statistics of France"

	Maps of France in 1830, multivariate datasets from A.-M. Guerry and others, and statistical and 
	graphic methods related to Guerry's "Moral Statistics of France". The goal is to facilitate the exploration and
	development of statistical and graphic methods for multivariate data in a geospatial context of historical interest.
	"""
	
	homepage = "https://github.com/friendly/Guerry"
	cran = "Guerry" 

	version("1.8.3", md5="effb31c0afc7508f7ee141e2dc29d0e0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
