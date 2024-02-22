# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPdc(RPackage):
	"""Permutation Distribution Clustering

	Permutation Distribution Clustering is a clustering method for time series. Dissimilarity of time series is formalized as the divergence between their permutation distributions. The permutation distribution was proposed as measure of the complexity of a time series.
	"""
	
	cran = "pdc" 

	version("1.0.3", md5="f086e59aff5f14fdf2678bb9f91f563e")

