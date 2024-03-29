# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCatfun(RPackage):
	"""Categorical Data Analysis

	Includes wrapper functions around existing functions for the analysis of categorical data and introduces functions for calculating risk differences and matched odds ratios. R currently supports a wide variety of tools for the analysis of categorical data. However, many functions are spread across a variety of packages with differing syntax and poor compatibility with each another. prop_test() combines the functions binom.test(), prop.test() and BinomCI() into one output. prop_power() allows for power and sample size calculations for both balanced and unbalanced designs. riskdiff() is used for calculating risk differences and matched_or() is used for calculating matched odds ratios. For further information on methods used that are not documented in other packages see Nathan Mantel and William Haenszel (1959) <doi:10.1093/jnci/22.4.719> and Alan Agresti (2002) <ISBN:0-471-36093-7>. 
	"""
	
	cran = "catfun" 

	version("0.1.4", md5="9b4d2bde547804459c3322e2deae5b60")

	depends_on("r-epitools", type=("build", "run"))
	depends_on("r-desctools", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
