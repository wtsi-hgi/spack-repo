# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPalr(RPackage):
	"""Colour Palettes for Data

	Colour palettes for data, based on some well known public data
    sets. Includes helper functions to map absolute values to known palettes, and 
    capture the work of image colour mapping as raster data sets. 
	"""
	
	homepage = "https://github.com/AustralianAntarcticDivision/palr"
	cran = "palr" 

	version("0.4.0", md5="a58440cad133ba506d936d997b82cdc0")

	depends_on("r@3.6:", type=("build", "run"))
