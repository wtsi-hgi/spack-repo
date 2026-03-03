# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RColorsgen(RPackage):
	"""Generation of Random Colors

	Generation of random colors, possibly with a given hue or a
    given luminosity. This is a port of the JavaScript library
    'randomColor' <https://randomcolor.lllllllllllllllll.com/>.
	"""
	
	homepage = "https://github.com/stla/colorsGen"
	cran = "colorsGen" 

	version("1.0.0", md5="13dcd64a084bcdcf44b67e4de4df2ece")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
