# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXpectr(RPackage):
	"""Generates Expectations for 'testthat' Unit Testing

	Helps systematize and ease the process of 
    building unit tests with the 'testthat' package by providing 
    tools for generating expectations.
	"""
	
	homepage = "https://github.com/ludvigolsen/xpectr"
	cran = "xpectr" 

	version("0.4.3", md5="ecbd9d2497eb5b4fa45a8e9c3eaf3046")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-clipr@0.7:", type=("build", "run"))
	depends_on("r-checkmate@2:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-fansi@0.4.1:", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rstudioapi@0.10:", type=("build", "run"))
	depends_on("r-testthat@2.3.1:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-withr@2:", type=("build", "run"))
