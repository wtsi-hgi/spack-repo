# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExcelfunctionsr(RPackage):
	"""Imports Excel Functions to R

	Implements 'Excel' functions in 'R' for your calculation simplicity.You can use most of the aggregate functions, addressing functions,logical functions and text functions. Helps you a ton in learning how 'R' works as some 'Excel' users might be struggling with the program.
	"""
	
	cran = "ExcelFunctionsR" 

	version("0.1.4", md5="27eea0f028ff976515eb55eca1752e98")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-roperators", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
