# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMixedindtests(RPackage):
	"""Tests of Randomness and Tests of Independence

	Functions for testing randomness for a univariate time series with arbitrary distribution  (discrete, continuous, mixture of both types) and for testing  independence between random variables with arbitrary distributions. The test statistics are based on the multilinear empirical copula and multipliers are used to compute P-values. The test of independence between random variables appeared in  Genest, Nešlehová, Rémillard & Murphy (2019) and the test of randomness appeared in Nasri (2022).
	"""
	
	cran = "MixedIndTests" 

	version("1.2.0", md5="d867fdcbb6b53f3ccbaa3613a085e66e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-copula", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-survey", type=("build", "run"))
