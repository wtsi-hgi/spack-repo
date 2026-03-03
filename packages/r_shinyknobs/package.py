# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinyknobs(RPackage):
	"""A Collection of Knob Inputs for 'shiny'

	A collection of highly configurable, touch-enabled knob input controls for 'shiny'. These components can be styled to fit in perfectly in any app, and allow users to set precise values through many input modalities. Users can touch-and-drag, click-and-drag, scroll their mouse wheel, double click, or use keyboard input.
	"""
	
	homepage = "https://github.com/cotepat/shinyKnobs"
	cran = "shinyKnobs" 

	version("0.1.3", md5="fa27c80346cfc08dfdcd2880f67ba441")

	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
