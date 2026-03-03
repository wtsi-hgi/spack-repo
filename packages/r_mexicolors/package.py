# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMexicolors(RPackage):
	"""Mexican Politics-Inspired Color Palette Generator

	A color palette generator inspired by Mexican politics, with 
    colors ranging from red on the left to gray in the middle and green on the 
    right. Palette options range from only a few colors to several colors, but with
    discrete and continuous options to offer greatest flexibility to the user. 
    This package allows for a range of applications, from mapping brief discrete scales 
    (e.g., four colors for Morena, PRI, and PAN) to continuous interpolated arrays 
    including dozens of shades graded from red to green.
	"""
	
	cran = "mexicolors" 

	version("0.2.0", md5="80c137f9ea9cd686a3307d27cb5cf4de")

