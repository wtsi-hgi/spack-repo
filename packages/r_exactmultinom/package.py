# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExactmultinom(RPackage):
	"""Multinomial Goodness-of-Fit Tests

	Computes exact p-values for multinomial goodness-of-fit tests based on multiple test statistics, namely, Pearson's chi-square, the log-likelihood ratio and the probability mass statistic. Implements the algorithm detailed in Resin (2020) <arXiv:2008.12682>. Estimates based on the classical asymptotic chi-square approximation or Monte-Carlo simulation can also be computed.
	"""
	
	cran = "ExactMultinom" 

	version("0.1.2", md5="78ce9096d408b3d4fee530053aea3829")

	depends_on("r-rcpp", type=("build", "run"))
