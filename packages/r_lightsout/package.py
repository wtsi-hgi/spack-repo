# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLightsout(RPackage):
	"""Implementation of the 'Lights Out' Puzzle Game

	Lights Out is a puzzle game consisting of a grid of lights
    that are either on or off. Pressing any light will toggle it and its
    adjacent lights. The goal of the game is to switch all the lights off. This
    package provides an interface to play the game on different board sizes,
    both through the command line or with a visual application. Puzzles can
    also be solved using the automatic solver included. View a demo
    online at <https://daattali.com/shiny/lightsout/>.
	"""
	
	homepage = "https://github.com/daattali/lightsout"
	cran = "lightsout" 

	version("0.3.2", md5="4bb6e23a606c60f2c746c38ae6ad9ddf")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-shiny@0.10:", type=("build", "run"))
	depends_on("r-shinyjs@0.3:", type=("build", "run"))
	depends_on("pandoc", type=("build", "link", "run"))
