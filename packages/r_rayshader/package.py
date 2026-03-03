# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRayshader(RPackage):
	"""Create Maps and Visualize Data in 2D and 3D

	Uses a combination of raytracing and multiple hill shading methods to produce 2D and 3D data visualizations and maps. Includes water detection and layering functions, programmable color palette generation, several built-in textures for hill shading, 2D and 3D plotting options, a built-in path tracer, 'Wavefront' OBJ file export, and the ability to save 3D visualizations to a 3D printable format.
	"""
	
	homepage = "https://www.rayshader.com"
	cran = "rayshader" 

	version("0.37.3", md5="7e5c976f9bfd4a31c58f0d28de5850d5")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-jpeg", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rgl@0.110.7:", type=("build", "run"))
	depends_on("r-terrainmeshr", type=("build", "run"))
	depends_on("r-rayimage@0.10:", type=("build", "run"))
	depends_on("r-rayvertex@0.10.4:", type=("build", "run"))
	depends_on("r-rayrender@0.32.2:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
