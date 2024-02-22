# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgredist(RPackage):
	"""Scales, Geometries, and Extensions of 'ggplot2' for Election
Mapping

	Provides 'ggplot2' extensions for political map making. Implements
    new geometries for groups of simple feature geometries. Adds palettes and scales 
    for red to blue color mapping and for discrete maps. Implements tools for easy 
    label generation and placement, automatic map coloring, and themes.
	"""
	
	homepage = "https://github.com/alarm-redist/ggredist"
	cran = "ggredist" 

	version("0.0.2", md5="a2d51014bb48a37b0be6aa3eebb46fd9")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
