# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLimnopalettes(RPackage):
	"""A Limnology Themed Palette Generator

	Palettes generated from limnology based field and laboratory photos. Palettes can be used to generate color values to be used in any functions that calls for a color (i.e. ggplot(), plot(), flextable(), etc.). 
	"""
	
	homepage = "https://github.com/SwampThingPaul/LimnoPalettes"
	cran = "LimnoPalettes" 

	version("0.1.0", md5="9688f338824bf7b7d5bc47dc98534cb0")

	depends_on("r@3:", type=("build", "run"))
