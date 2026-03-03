# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLandcomp(RPackage):
	"""Analysing Landscape Composition and Structure at Multiple Scales

	Changes of landscape diversity and structure can be detected
    soon if relying on landscape class combinations and analysing patterns
    at multiple scales. 'LandComp' provides such an opportunity, based on
    Juhász-Nagy's functions (Juhász-Nagy P, Podani J 1983
    <doi:10.1007/BF00129432>). Functions can handle multilayered data.
    Requirements of the input: binary data contained by a regular square
    or hexagonal grid, and the grid should have projected coordinates.
	"""
	
	homepage = "https://github.com/ladylavender/LandComp"
	cran = "LandComp" 

	version("0.0.5", md5="08fd5c6f9aa8552852398bf1e907ad5d")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
