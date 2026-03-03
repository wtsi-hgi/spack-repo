# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmfilter(RPackage):
	"""Filtering Algorithms for the State Space Models on the Stiefel
Manifold

	Provides the filtering algorithms for the state space models on the Stiefel manifold as well as the corresponding sampling algorithms for uniform, vector Langevin-Bingham and matrix Langevin-Bingham distributions on the Stiefel manifold.
	"""
	
	homepage = "https://github.com/yukai-yang/SMFilter"
	cran = "SMFilter" 

	version("1.0.3", md5="e775dbe348cbc74d7bbcfecd2d45b865")

	depends_on("r@3:", type=("build", "run"))
