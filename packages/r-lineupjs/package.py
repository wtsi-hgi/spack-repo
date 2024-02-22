# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLineupjs(RPackage):
	"""'HTMLWidget' Wrapper of 'LineUp' for Visual Analysis of
Multi-Attribute Rankings

	'LineUp' is an interactive technique designed to create, visualize and explore rankings of items based on a set of heterogeneous attributes.
  This is a 'htmlwidget' wrapper around the JavaScript library 'LineUp.js'.
  It is designed to be used in 'R Shiny' apps and 'R Markddown' files.
  Due to an outdated 'webkit' version of 'RStudio' it won't work in the integrated viewer.
	"""
	
	homepage = "https://github.com/lineupjs/lineup_htmlwidget/"
	cran = "lineupjs" 

	version("4.6.0", md5="577ad1c5f86c7cf466ba167080708747")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
