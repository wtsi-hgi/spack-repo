# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RColour(RPackage):
	"""Create Colour Palettes from Images

	Can take in images in either .jpg, .jpeg, or .png format and creates a colour palette of the most frequent colours used in the image. Also provides some custom colour palettes.
	"""
	
	cran = "colouR" 

	version("0.1.1", md5="2af8c69828a263d1c453f1b85b7d83d9")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-jpeg", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-pixmap", type=("build", "run"))
