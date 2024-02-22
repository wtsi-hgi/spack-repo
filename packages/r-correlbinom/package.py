# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCorrelbinom(RPackage):
	"""Correlated Binomial Probabilities

	Calculates the probabilities of k successes given n trials of a binomial random variable with non-negative correlation across trials. The function takes as inputs the scalar values the level of correlation or association between trials, the success probability, the number of trials, an optional input specifying the number of bits of precision used in the calculation, and an optional input specifying whether the calculation approach to be used is from Witt (2014) <doi:10.1080/03610926.2012.725148> or from Kuk (2004) <doi:10.1046/j.1467-9876.2003.05369.x>. The output is a (trials+1)-dimensional vector containing the likelihoods of 0, 1, ..., trials successes.
	"""
	
	cran = "correlbinom" 

	version("0.0.1", md5="ee24d878eaeb2549cbaab9c16ed506fb")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-rmpfr", type=("build", "run"))
