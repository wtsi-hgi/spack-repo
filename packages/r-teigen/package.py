# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTeigen(RPackage):
	"""Model-Based Clustering and Classification with the Multivariate
t Distribution

	Fits mixtures of multivariate t-distributions (with eigen-decomposed covariance structure) via the expectation conditional-maximization algorithm under a clustering or classification paradigm.
	"""
	
	cran = "teigen" 

	version("2.2.2", md5="2d0c663f943d08b775963edc620f99d5")

