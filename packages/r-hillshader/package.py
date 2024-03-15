# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHillshader(RPackage):
	"""Create Hillshade Relief Maps Using Ray-Tracing

	A set of tools to create georeferenced hillshade relief 
    raster maps using ray-tracing and other advanced hill-shading 
    techniques. It includes a wrapper function to create a georeferenced,
    ray-traced hillshade map from a digital elevation model, and other
    functions that can be used in a rayshader pipeline. 
	"""
	
	cran = "hillshader" 

	version("0.1.2", md5="7f0b785461c757d3845753f53ddd6fbf")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-rayshader", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
