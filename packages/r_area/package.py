# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArea(RPackage):
	"""Calculate Area of Triangles and Polygons

	Calculate the area of triangles and polygons using the shoelace 
 formula. Area may be signed, taking into account path orientation, or unsigned, 
 ignoring path orientation. The shoelace formula is described at 
 <https://en.wikipedia.org/wiki/Shoelace_formula>. 
	"""
	
	homepage = "https://github.com/hypertidy/area"
	cran = "area" 

	version("0.2.0", md5="8357663521850d7a60fe06a5ab263ae1")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-cpp11", type=("build", "run"))
