# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFoodwebwrapper(RPackage):
	"""Enhanced Wrapper to Show Which Functions Call What

	Enhances the functionality of the mvbutils::foodweb() program. The matrix-format output of the original program contains identical row names and column names, each name representing a retrieved function. This format is enhanced by using the find_funs() program [see Sebastian (2017) <https://sebastiansauer.github.io/finds_funs/>] to concatenate the package name to the function name. Each package is assigned a unique color, that is used to color code the text naming the packages and the functions. This color coding is extended to the entries of value "1" within the matrix, indicating the pattern of ancestor and descendent functions.
	"""
	
	cran = "foodwebWrapper" 

	version("1.1.0", md5="2719136981c8c64c83f9dd2c0c9ac867")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-mvbutils", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-r2html", type=("build", "run"))
	depends_on("r-textshaping", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
