# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTerrainmeshr(RPackage):
	"""Triangulate and Simplify 3D Terrain Meshes

	Provides triangulations of regular height fields, based on the methods described in "Fast Polygonal Approximation of Terrains and Height Fields" Michael Garland and Paul S. Heckbert (1995) <https://www.mgarland.org/files/papers/scape.pdf> using code from the 'hmm' library written by Michael Fogleman <https://www.github.com/fogleman/hmm>.
	"""
	
	homepage = "https://www.github.com/tylermorganwall/terrainmeshr"
	cran = "terrainmeshr" 

	version("0.1.0", md5="0af22f4a878b52273aa6d9c31f1316c6")

	depends_on("r-rcpp", type=("build", "run"))
