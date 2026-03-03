# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCoop(RPackage):
	"""Co-Operation: Fast Covariance, Correlation, and Cosine
Similarity Operations

	Fast implementations of the co-operations: covariance,
    correlation, and cosine similarity.  The implementations are
    fast and memory-efficient and their use is resolved
    automatically based on the input data, handled by R's S3
    methods.  Full descriptions of the algorithms and benchmarks
    are available in the package vignettes.
	"""
	
	homepage = "https://github.com/wrathematics/coop"
	cran = "coop" 

	version("0.6-3", md5="b6e2755b67964b2fb4f204c6a9ef944c")

	depends_on("r@3.1:", type=("build", "run"))
