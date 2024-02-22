# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPoolbal(RPackage):
	"""Balancing Central and Marginal Rejection of Pooled p-Values

	When using pooled p-values to adjust for multiple testing, there is an inherent balance that must be struck between rejection based on weak evidence spread among many tests and strong evidence in a few, explored in Salahub and Olford (2023) <arXiv:2310.16600>. This package provides functionality to compute marginal and central rejection levels and the centrality quotient for p-value pooling functions and provides implementations of the chi-squared quantile pooled p-value (described in Salahub and Oldford (2023)) and a proposal from Heard and Rubin-Delanchy (2018) <doi:10.1093/biomet/asx076> to control the quotient's value.
	"""
	
	cran = "PoolBal" 

	version("0.1-0", md5="cb0ed2c7124f02e482163f5b0624c752")

	depends_on("r@4.3:", type=("build", "run"))
