# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMove(RPackage):
	"""Visualizing and Analyzing Animal Track Data

	Contains functions to access movement data stored in 'movebank.org'
    as well as tools to visualize and statistically analyze animal movement data,
    among others functions to calculate dynamic Brownian Bridge Movement Models.
    Move helps addressing movement ecology questions.
	"""
	
	homepage = "https://bartk.gitlab.io/move/"
	cran = "move" 

	version("4.2.4", md5="a9cd8ddd8fec958f787aff0782ee71da")

	depends_on("r-geosphere@1.4.3:", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-raster@3.6.14:", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
