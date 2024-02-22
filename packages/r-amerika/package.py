# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAmerika(RPackage):
	"""American Politics-Inspired Color Palette Generator

	A color palette generator inspired by American politics, with colors ranging from blue on the 
    left to gray in the middle and red on the right. A variety of palettes allow for a range of applications 
    from brief discrete scales (e.g., three colors for Democrats, Independents, and Republicans) to 
    continuous interpolated arrays including dozens of shades graded from blue (left) to red (right). This
    package greatly benefitted from building on the source code (with permission) from Ram and Wickham (2015).
	"""
	
	cran = "amerika" 

	version("0.1.0", md5="393e32753f9cc46e113f4510c36846cf")

