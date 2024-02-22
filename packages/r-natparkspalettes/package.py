# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNatparkspalettes(RPackage):
	"""Color Palettes Inspired by National Parks

	Color palettes for data visualization inspired by National Parks. Currently contains 15 color schemes and checks for colorblind-friendliness of palettes.
	"""
	
	homepage = "https://github.com/kevinsblake/NatParksPalettes"
	cran = "NatParksPalettes" 

	version("0.2.0", md5="e842dcfb763f1607740125be1a777f78")

	depends_on("r-ggplot2", type=("build", "run"))
