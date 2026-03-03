# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinyaframe(RPackage):
	"""'WebVR' Data Visualizations with 'RStudio Shiny' and 'Mozilla
A-Frame'

	Make R data available in Web-based virtual reality experiences
  for immersive, cross-platform data visualizations. Includes the 'gg-aframe'
  JavaScript package for a Grammar of Graphics declarative HTML syntax to create
  3-dimensional data visualizations with 'Mozilla A-Frame' <https://aframe.io>.
	"""
	
	cran = "shinyaframe" 

	version("1.0.1", md5="0cfad7fa4a065d3bb348138bdd3b725d")

	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
