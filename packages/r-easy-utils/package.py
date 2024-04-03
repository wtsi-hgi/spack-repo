# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REasyUtils(RPackage):
	"""Frequently Used Functions for Easy R Programming

	Some utility functions for validation, data manipulation or color palettes. These functions can be helpful to reduce internal codes everywhere in package development.
	"""
	
	homepage = "https://github.com/ycli1995/easy.utils"
	cran = "easy.utils" 

	version("0.0.3", md5="193866ee4e79e427eef71426a8eb2347")
	version("0.0.4", md5="e8465c5bedfef1fd75fb0d13f4256774")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-fastmatch", type=("build", "run"))
	depends_on("r-polychrome", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
