# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMyStepwise(RPackage):
	"""Stepwise Variable Selection Procedures for Regression Analysis

	The stepwise variable selection procedure (with iterations
 between the 'forward' and 'backward' steps) can be used to obtain
 the best candidate final regression model in regression analysis.
 All the relevant covariates are put on the 'variable list' to be
 selected. The significance levels for entry (SLE) and for stay
 (SLS) are usually set to 0.15 (or larger) for being conservative.
 Then, with the aid of substantive knowledge, the best candidate
 final regression model is identified manually by dropping the
 covariates with p value > 0.05 one at a time until all regression
 coefficients are significantly different from 0 at the chosen alpha
 level of 0.05.
	"""
	
	cran = "My.stepwise" 

	version("0.1.0", md5="5a53bfd8b319bebdadf4fabce64a14e0")

	depends_on("r@3.3.3:", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
