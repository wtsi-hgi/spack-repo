# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRayvertex(RPackage):
	"""3D Software Rasterizer

	Rasterize images using a 3D software renderer. 3D scenes are created either by importing external files, building scenes out of the included objects, or by constructing meshes manually. Supports point and directional lights, anti-aliased lines, shadow mapping, transparent objects, translucent objects, multiple materials types, reflection, refraction, environment maps, multicore rendering, bloom, tone-mapping, and screen-space ambient occlusion.
	"""
	
	homepage = "https://www.rayvertex.com"
	cran = "rayvertex" 

	version("0.10.4", md5="7cadb65801d29d53ff02857fc1cbeffc")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rayimage", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-spacefillr", type=("build", "run"))
	depends_on("r-rcppthread", type=("build", "run"))
