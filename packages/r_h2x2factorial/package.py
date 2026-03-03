# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RH2x2factorial(RPackage):
	"""Sample Size Calculation in Hierarchical 2x2 Factorial Trials

	Implements the sample size methods for hierarchical 2x2 factorial trials under two choices of effect estimands and a series of hypothesis tests proposed in "Sample size calculation in hierarchical 2x2 factorial trials with unequal cluster sizes" (under review), and provides the table and plot generators for the sample size estimations.
	"""
	
	cran = "H2x2Factorial" 

	version("2.0.0", md5="2238e22f4eeb5ebba801cec3266f2364")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
