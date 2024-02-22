# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShide(RPackage):
	"""Date/Time Classes Based on Jalali Calendar

	Implements S3 classes for storing dates and date-times based on the Jalali calendar. 
    The main design goal of 'shide' is consistency with base R's 'Date' and 'POSIXct'.
    It provide features such as: date-time parsing, formatting and arithmetic.
	"""
	
	homepage = "https://github.com/mmollayi/shide"
	cran = "shide" 

	version("0.1.3", md5="492f98a07d6be81eafac8419f9c46db5")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tzdb", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-cpp11", type=("build", "run"))
