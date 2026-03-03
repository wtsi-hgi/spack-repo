# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPalette(RPackage):
	"""Color Scheme Helpers

	Hexadecimal codes are typically used to represent colors in R.
    Connecting these codes to their colors requires practice or memorization.
    'palette' provides a 'vctrs' class for working with color palettes, including
    printing and plotting functions. The goal of the class is to place visual
    representations of color palettes directly on or, at least, next to their
    corresponding character representations. Palette extensions also are provided
    for data frames using 'pillar'.
	"""
	
	homepage = "https://github.com/christopherkenny/palette"
	cran = "palette" 

	version("0.0.2", md5="53acca096f60ffc44cf3362af4f9910d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-pillar", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
