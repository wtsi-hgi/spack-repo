# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPnwcolors(RPackage):
	"""Color Palettes Inspired by Nature in the US Pacific Northwest

	PNW-Inspired Palettes for 'R' data visualizations. Palettes are variable 
	in length and checked for colorblind accessibility from hue, saturation, 
	and lightness value scaling using the 'Chroma.js  Color Palette Helper' 
	<https://gka.github.io/palettes/>.
	"""
	
	homepage = "https://github.com/jakelawlor/PNWColors"
	cran = "PNWColors" 

	version("0.1.0", md5="84bb4e680513f39af17d5a9f2e3d9c61")

