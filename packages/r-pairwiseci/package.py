# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPairwiseci(RPackage):
	"""Confidence Intervals for Two Sample Comparisons

	Calculation of the parametric, nonparametric confidence intervals
 for the difference or ratio of location parameters, nonparametric confidence interval
 for the Behrens-Fisher problem and for the difference, ratio and odds-ratio of binomial
 proportions for comparison of independent samples. Common wrapper functions to split 
 data sets and apply confidence intervals or tests to these subsets.
 A by-statement allows calculation of CI separately for the levels of further factors. 
 CI are not adjusted for multiplicity.
	"""
	
	cran = "pairwiseCI" 

	version("0.1-27", md5="d1a5f7cf95425c0e2a22797a07ae3f61")

	depends_on("r-mcpan", type=("build", "run"))
	depends_on("r-coin@1.3.0:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mcprofile", type=("build", "run"))
