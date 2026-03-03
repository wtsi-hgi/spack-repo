# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSearchtrees(RPackage):
	"""Spatial Search Trees

	The QuadTree data structure is useful for fast,
	     neighborhood-restricted lookups. We use it to implement fast k-Nearest
        Neighbor and Rectangular range lookups in 2 dimenions. The
        primary target is high performance interactive graphics.
	"""
	
	homepage = "https://github.com/gmbecker/SearchTrees"
	cran = "SearchTrees" 

	version("0.5.5", md5="5b4281e11849c6e7223ec586b25f3780")

