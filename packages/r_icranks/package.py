# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIcranks(RPackage):
	"""Simultaneous Confidence Intervals for Ranks

	Algorithms to construct simultaneous confidence intervals for the ranks of means mu_1,...,mu_n based on an independent Gaussian sample using multiple testing techniques. 
	"""
	
	cran = "ICRanks" 

	version("3.1", md5="63ffb14fbd45fe7c0157ad759b703959")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-multcomp", type=("build", "run"))
	depends_on("r-gmp", type=("build", "run"))
