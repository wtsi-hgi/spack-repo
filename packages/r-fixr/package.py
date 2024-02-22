# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFixr(RPackage):
	"""Fixing Data Made Easy for Statistical Analysis

	A set of functions that facilitate basic data manipulation and cleaning for statistical analysis including functions for finding and fixing duplicate rows and columns, missing values, outliers, and special characters in column and row names and functions for checking data consistency, distribution, quality, reliability, and structure.
	"""
	
	homepage = "https://github.com/ambuvjyn/fixr"
	cran = "fixr" 

	version("0.1.0", md5="621e0001ade0503b7768e187d5abcaf0")

	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
