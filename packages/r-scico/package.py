# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScico(RPackage):
	"""Colour Palettes Based on the Scientific Colour-Maps

	Colour choice in information visualisation is important in order to
    avoid being mislead by inherent bias in the used colour palette. The 'scico'
    package provides access to the perceptually uniform and colour-blindness 
    friendly palettes developed by Fabio Crameri and released under the 
    "Scientific Colour-Maps" moniker. The package contains 24 different palettes 
    and includes both diverging and sequential types.
	"""
	
	homepage = "https://github.com/thomasp85/scico"
	cran = "scico" 

	version("1.5.0", md5="6d7b46235973e32b01a6b5edcf1629eb")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
