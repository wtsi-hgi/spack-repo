# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLegocolors(RPackage):
	"""Official Lego Color Palettes

	Provides a dataset containing several color naming conventions established by multiple sources, along with associated color metadata.
    The package also provides related helper functions for mapping among the different Lego color naming conventions and between Lego colors, hex colors, and 'R' color names, 
    making it easy to convert any color palette to one based on existing Lego colors while keeping as close to the original color palette as possible.
    The functions use nearest color matching based on Euclidean distance in RGB space. 
    Naming conventions for color mapping include those from 'BrickLink' (<https://www.bricklink.com>), 'The Lego Group' (<https://www.lego.com>), 'LDraw' (<https://www.ldraw.org/>), and 'Peeron' (<http://www.peeron.com/>).
	"""
	
	homepage = "https://github.com/leonawicz/legocolors"
	cran = "legocolors" 

	version("0.3.1", md5="269d660dd06f01a6d98ae30926c26987")

	depends_on("r@2.10:", type=("build", "run"))
