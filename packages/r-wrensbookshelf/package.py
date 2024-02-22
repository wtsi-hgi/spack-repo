# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWrensbookshelf(RPackage):
	"""A Collection of Palettes and Some Functions to Help Use Them

	A collection of color palettes that were extracted from various books on my sons(Wren) bookshelf. Also included are a number of functions and wrappers to utilize them, as well as to subset the palettes to desired number/specific colors.
	"""
	
	homepage = "https://github.com/buveges/WrensBookshelf"
	cran = "WrensBookshelf" 

	version("0.1.0", md5="9d9b6fdf782b50f949c9271029d21f69")

	depends_on("r-ggplot2", type=("build", "run"))
