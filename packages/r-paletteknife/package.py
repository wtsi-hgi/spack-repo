# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPaletteknife(RPackage):
	"""Create Colour Scales and Legend from Continuous or Categorical
Vectors

	Streamlines the steps for adding colour scales and associated legends 
         when working with base R graphics, especially for interactive use. Popular
         palettes are included and pretty legends produced when mapping a large 
         variety of vector classes to a colour scale. An additional helper for 
         adding axes and grid lines complements the base::plot() work flow.
	"""
	
	homepage = "https://github.com/johnxhobbs/paletteknife"
	cran = "paletteknife" 

	version("0.4.2", md5="7f6cb74dbe0aa0a535ae704d76d10216")

