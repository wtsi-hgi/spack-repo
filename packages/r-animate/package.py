# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnimate(RPackage):
	"""A Web-Based Graphics Device for Animated Visualisations

	Implements a web-based graphics device for animated visualisations.
  Modelled on the 'base' syntax, it extends the 'base' graphics functions to
  support frame-by-frame animation and keyframes animation.
  The target use cases are real-time animated visualisations, including agent-based
  models, dynamical systems, and animated diagrams.
  The generated visualisations can be deployed as GIF images / MP4 videos, as
  'Shiny' apps (with interactivity) or as HTML documents through embedding into
  R Markdown documents.
	"""
	
	homepage = "https://kcf-jackson.github.io/animate/"
	cran = "animate" 

	version("0.3.9.4", md5="a24146d607255e1645d248819476f306")

	depends_on("r-r6", type=("build", "run"))
	depends_on("r-httpuv", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
