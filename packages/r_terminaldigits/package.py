# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTerminaldigits(RPackage):
	"""Tests of Uniformity and Independence for Terminal Digits

	Implements simulated tests for the hypothesis that terminal digits are uniformly
    distributed (chi-squared goodness-of-fit) and the hypothesis that terminal digits
    are independent from preceding digits (several tests of independence for r x c 
    contingency tables). Also, for a number of distributions, implements Monte Carlo 
    simulations for type I errors and power for the test of independence. 
	"""
	
	cran = "terminaldigits" 

	version("0.1.0", md5="39bbedc71188ec0b8a032c527dbde914")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-discretefit", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
