# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrayons(RPackage):
	"""Color Palettes from Crayon Boxes

	Provides color palettes based on crayon colors since the early 1900s. 
    Colors are based on various crayon colors, sets, and promotional palettes, most of
    which can be found at <https://en.wikipedia.org/wiki/List_of_Crayola_crayon_colors>. All 
    palettes are discrete palettes and are not necessarily color-blind friendly. 
    Provides scales for 'ggplot2' for discrete coloring.
	"""
	
	homepage = "https://github.com/christopherkenny/crayons"
	cran = "crayons" 

	version("0.0.2", md5="13a3b06bd894044a8e17b9a63295f053")
	version("0.0.3", md5="366b8f40ecaa9dae73108b5bd26eded4")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-palette", type=("build", "run"))
