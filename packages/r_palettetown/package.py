# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPalettetown(RPackage):
	"""Use Pokemon Inspired Colour Palettes

	Use Pokemon(R) inspired palettes with additional 'ggplot2' scales.
    Palettes are the colours in each Pokemon's sprite, ordered by how common
    they are in the image. The first 386 Pokemon are currently provided.
	"""
	
	homepage = "https://github.com/timcdlucas/palettetown"
	cran = "palettetown" 

	version("0.1.1", md5="7e4ab4c18e1b48cd6771a3fc4a42ac6f")

