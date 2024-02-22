# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPcra(RPackage):
	"""Companion to Portfolio Construction and Risk Analysis

	A collection of functions and data sets that support teaching
  a quantitative finance MS level course on Portfolio Construction and Risk
  Analysis, and the writing of a textbook for such a course.  The package is
  unique in providing several real-world data sets that may be used for problem
  assignments and student projects.  The data sets include cross-sections of
  stock data from the Center for Research on Security Prices, LLC (CRSP),
  corresponding factor exposures data from S&P Global, and several SP500 data
  sets.
	"""
	
	cran = "PCRA" 

	version("1.2", md5="9c286f764c8b850af185d91101ebc67d")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-performanceanalytics", type=("build", "run"))
	depends_on("r-portfolioanalytics", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-robstattm", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-r-cache", type=("build", "run"))
