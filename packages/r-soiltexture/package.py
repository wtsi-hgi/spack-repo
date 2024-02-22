# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSoiltexture(RPackage):
	"""Functions for Soil Texture Plot, Classification and
Transformation

	"The Soil Texture Wizard" is a set of R functions designed to produce texture triangles (also called texture plots, texture diagrams, texture ternary plots), classify and transform soil textures data. These functions virtually allows to plot any soil texture triangle (classification) into any triangle geometry (isosceles, right-angled triangles, etc.). This set of function is expected to be useful to people using soil textures data from different soil texture classification or different particle size systems. Many (> 15) texture triangles from all around the world are predefined in the package. A simple text based graphical user interface is provided: soiltexture_gui().
	"""
	
	homepage = "https://github.com/julienmoeys/soiltexture"
	cran = "soiltexture" 

	version("1.5.3", md5="62f0ae6091664aab33d5c16c24482fe6")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
