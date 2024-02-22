# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRandmeta(RPackage):
	"""Efficient Numerical Algorithm for Exact Inference in Meta
Analysis

	A novel numerical algorithm that provides functionality for estimating the exact 95% confidence interval of the location parameter in the random effects model, and is much faster than the naive method. Works best when the number of studies is between 6-20.
	"""
	
	cran = "RandMeta" 

	version("0.1.0", md5="3588fe6dd5640a758a1944d3e3cf0e11")

	depends_on("r@2.10:", type=("build", "run"))
