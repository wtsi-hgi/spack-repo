# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMvmesh(RPackage):
	"""Multivariate Meshes and Histograms in Arbitrary Dimensions

	Define, manipulate and plot meshes on simplices, spheres, balls, rectangles and tubes.
 Directional and other multivariate histograms are provided.
	"""
	
	cran = "mvmesh" 

	version("1.6", md5="6580c2a658ce67d745507a71e4cd01de")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcdd", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-geometry", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-simplicialcubature", type=("build", "run"))
