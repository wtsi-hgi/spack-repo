# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTablet(RPackage):
	"""Tabulate Descriptive Statistics in Multiple Formats

	Creates a table of descriptive statistics
 for factor and numeric columns in a data frame. Displays
 these by groups, if any. Highly customizable, with support
 for 'html' and 'pdf' provided by 'kableExtra'. Respects
 original column order, column labels, and factor level order.
 See ?tablet.data.frame and vignettes.
	"""
	
	cran = "tablet" 

	version("0.6.8", md5="6b2b4b5c79916d9cd49dea223a1fec23")
	version("0.6.5", md5="1d903d378abacb530e4bced5a60b5a0a")

	depends_on("r-dplyr@1.0.2:", type=("build", "run"))
	depends_on("r-yamlet@0.10.21:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-kableextra@0.9:", type=("build", "run"))
	depends_on("r-spork@0.2.7:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-reactable", type=("build", "run"))
