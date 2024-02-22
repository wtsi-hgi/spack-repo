# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIndustrial(RPackage):
	"""Data, Functions and Support Materials from the Book "industRial
Data Science"

	Companion package to the book "industRial data science", 
    J.Ramalho (2021) <https://j-ramalho.github.io/industRial/>. 
    Provides data sets and functions to complete the case studies and contains 
    the book original Rmd files and tutorials.
	"""
	
	homepage = "https://github.com/J-Ramalho/industRial"
	cran = "industRial" 

	version("0.1.0", md5="abed63d3fb52cb8c839f8b41fd2a200e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-sixsigma", type=("build", "run"))
