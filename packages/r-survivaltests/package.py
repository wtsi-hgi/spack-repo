# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurvivaltests(RPackage):
	"""Survival Tests for One-Way Layout

	Performs survival analysis for one-way layout. The package includes the generalized test for survival ANOVA (Tsui and Weerahandi (1989) <doi:10.2307/2289949> and (Weerahandi, 2004; ISBN:978-0471470175)). It also performs pairwise comparisons and graphical approaches. Moreover, it assesses the weibullness of data in each group via test. The package computes mean and confidence interval under Weibull distribution.
	"""
	
	cran = "SurvivalTests" 

	version("1.0", md5="ce9b9497f828d4ba187aba7375f18e38")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-weibullness", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
