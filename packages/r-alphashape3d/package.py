# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAlphashape3d(RPackage):
	"""Implementation of the 3D Alpha-Shape for the Reconstruction of
3D Sets from a Point Cloud

	Implementation in R of the alpha-shape of a finite set of points in the three-dimensional space. The alpha-shape generalizes the convex hull and allows to recover the shape of non-convex and even non-connected sets in 3D, given a random sample of points taken into it. Besides the computation of the alpha-shape, this package provides users with functions to compute the volume of the alpha-shape, identify the connected components and facilitate the three-dimensional graphical visualization of the estimated set. 
	"""
	
	cran = "alphashape3d" 

	version("1.3.2", md5="5bb0a068adf0c817e38eaa0e724c6e6d")

	depends_on("r-geometry", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-rann", type=("build", "run"))
