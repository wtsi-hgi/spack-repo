# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUnifir(RPackage):
	"""A Unifying API for Calling the 'Unity' '3D' Video Game Engine

	Functions for the creation and manipulation of scenes and objects
    within the 'Unity' '3D' video game engine (<https://unity.com/>). Specific
    focuses include the creation and import of terrain data and 'GameObjects' as
    well as scene management.
	"""
	
	homepage = "https://docs.ropensci.org/unifir/"
	cran = "unifir" 

	version("0.2.4", md5="4b3166450df12967758421119b9f22fb")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-proceduralnames", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
