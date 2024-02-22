# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCubeview(RPackage):
	"""View 3D Raster Cubes Interactively

	Creates a 3D data cube view of a RasterStack/Brick, typically a 
    collection/array of RasterLayers (along z-axis) with the same geographical 
    extent (x and y dimensions) and resolution, provided by package 'raster'. 
    Slices through each dimension (x/y/z), freely adjustable in location, 
    are mapped to the visible sides of the cube. The cube can be freely rotated. 
    Zooming and panning can be used to focus on different areas of the cube.
	"""
	
	cran = "cubeview" 

	version("0.2.0", md5="914492b92ac4351c0bd54f394f8265f9")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-stars", type=("build", "run"))
	depends_on("r-viridislite", type=("build", "run"))
