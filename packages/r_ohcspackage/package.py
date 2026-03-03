# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROhcspackage(RPackage):
	"""Prepare Housing Data for Analysis

	Prepares census and core housing needs data, specifically designed for use with Statistics Canada data and standardized input data. The package offers functions for tidying, organizing, and splitting complex data tables, making it easier for users to perform analyses on the data. 'OHCSpackage''' is particularly useful for those working with census data that has a consistent format, number of rows, and number of columns. With this package, users can save time and streamline their data preparation processes.
	"""
	
	cran = "OHCSpackage" 

	version("0.1.5", md5="62ebc712ce2e3630c51baacf3c37f533")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
