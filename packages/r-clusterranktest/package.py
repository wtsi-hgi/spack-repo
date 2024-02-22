# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClusterranktest(RPackage):
	"""Rank Tests for Clustered Data

	Nonparametric rank based tests (rank-sum tests and signed-rank tests) for clustered data, especially useful for clusters having informative cluster size and intra-cluster group size.
	"""
	
	cran = "ClusterRankTest" 

	version("1.0", md5="9c8f9eccb76859387c1810ed47621ec6")

