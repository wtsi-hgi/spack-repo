# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSur(RPackage):
	"""Companion to "Statistics Using R: An Integrative Approach"

	Access to the datasets and many of the functions used in "Statistics Using R: An Integrative Approach". These datasets include a subset of the National Education Longitudinal Study, the Framingham Heart Study, as well as several simulated datasets used in the examples throughout the textbook. The functions included in the package reproduce some of the functionality of 'Stata' that is not directly available in 'R'.  The package also contains a tutorial on basic data frame management, including how to handle missing data.
	"""
	
	cran = "sur" 

	version("1.0.4", md5="24a5553ae80ecaf937ad5794426b53fa")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-learnr", type=("build", "run"))
