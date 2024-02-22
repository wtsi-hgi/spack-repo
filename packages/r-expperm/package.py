# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExpperm(RPackage):
	"""Computing Expectations and Marginal Likelihoods for Permutations

	A set of functions for computing expected permutation matrices given a matrix of likelihoods for each individual assignment. It has been written to accompany the forthcoming paper 'Computing expectations and marginal likelihoods for permutations'. Publication details will be updated as soon as they are finalized.
	"""
	
	cran = "expperm" 

	version("1.6", md5="23dad3a86302e790aa45e8027cc8059a")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
