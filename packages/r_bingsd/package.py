# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBingsd(RPackage):
	"""Calculation for Single Arm Group Sequential Test with Binary
Endpoint

	Consider an at-most-K-stage group sequential design with only an upper bound for the last analysis and non-binding lower bounds.With binary endpoint, two kinds of test can be applied, asymptotic test based on normal distribution and exact test based on binomial distribution. This package supports the computation of boundaries and conditional power for single-arm group sequential test with binary endpoint, via either asymptotic or exact test. The package also provides functions to obtain boundary crossing probabilities given the design.
	"""
	
	cran = "BinGSD" 

	version("0.0.1", md5="8c4d33fd06487546a44fdf716cfaef99")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mvtnorm@1.0.11:", type=("build", "run"))
