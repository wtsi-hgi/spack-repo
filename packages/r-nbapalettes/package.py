# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNbapalettes(RPackage):
	"""An NBA Jersey Palette Generator

	Palettes generated from NBA jersey colorways.
	"""
	
	homepage = "https://github.com/murrayjw/nbapalettes"
	cran = "nbapalettes" 

	version("0.1.0", md5="55036b0d5c9c7a0269b044d1a293fb6e")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
