# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAutoimage(RPackage):
	"""Multiple Heat Maps for Projected Coordinates

	Functions for displaying multiple images  or scatterplots with a color 
    scale, i.e., heat maps, possibly with projected coordinates.  The
    package relies on the base graphics system, so graphics are
    rendered rapidly.
	"""
	
	cran = "autoimage" 

	version("2.2.3", md5="08559cb0b829a155b2d82dd25bb5ea58")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-mapproj", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-maps", type=("build", "run"))
	depends_on("r-mba", type=("build", "run"))
