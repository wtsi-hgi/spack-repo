# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimplecolors(RPackage):
	"""Access Color Names Using a Standardized Nomenclature

	A curated set of colors that are called using
    a standardized syntax: saturation + hue + lightness. For example, 
    "brightblue4" and "mutedred2". Functions exists to return individual colors 
    by name or to build palettes across or within hues. Most functions allow you 
    to visualize the palettes in addition to returning the desired hex codes.
	"""
	
	homepage = "https://github.com/rjake/simplecolors"
	cran = "simplecolors" 

	version("0.1.2", md5="024e552f7e45e61dcca8c1b9c4fdd820")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
