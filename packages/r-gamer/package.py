# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGamer(RPackage):
	"""Color Palettes Inspired by Video Games

	Palettes based on video games.
	"""
	
	homepage = "https://www.constantine-cooke.com/gameR/"
	cran = "gameR" 

	version("0.0.5", md5="d312562b72fd732c195ce24009ad1110")

