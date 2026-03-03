# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNord(RPackage):
	"""Arctic Ice Studio's Nord and Group of Seven Inspired Colour
Palettes for 'ggplot2'

	Provides the Arctic Ice Studio's Nord and Group of Seven inspired colour palettes for use with 'ggplot2' via custom functions.
	"""
	
	cran = "nord" 

	version("1.0.0", md5="cb718f6e998514d7e57fa2119e270c7d")

	depends_on("r-ggplot2", type=("build", "run"))
