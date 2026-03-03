# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMorph(RPackage):
	"""3D Segmentation of Voxels into Morphologic Classes

	Automatically segments a 3D array of voxels into mutually exclusive morphological elements. This package extends existing work for segmenting 2D binary raster data. A paper documenting this approach has been accepted for publication in the journal Landscape Ecology. Detailed references will be updated here once those are known.
	"""
	
	cran = "morph" 

	version("1.1.0", md5="94ffaa09e0acc26fc6e1ff3a65f18da3")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
