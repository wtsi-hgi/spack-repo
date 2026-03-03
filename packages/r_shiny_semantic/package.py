# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinySemantic(RPackage):
	"""Semantic UI Support for Shiny

	Creating a great user interface for your Shiny apps can be a
    hassle, especially if you want to work purely in R and don't want to
    use, for instance HTML templates. This package adds support for a
    powerful UI library Fomantic UI - <https://fomantic-ui.com/> (before
    Semantic). It also supports universal UI input binding that works with
    various DOM elements.
	"""
	
	homepage = "https://appsilon.github.io/shiny.semantic/"
	cran = "shiny.semantic" 

	version("0.5.0", md5="36393f0f2ff2e1ba14c4fbf1864a2460")

	depends_on("r-glue", type=("build", "run"))
	depends_on("r-htmltools@0.2.6:", type=("build", "run"))
	depends_on("r-htmlwidgets@0.8:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr@0.2.2:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-semantic-assets@1.1:", type=("build", "run"))
	depends_on("r-shiny@0.12.1:", type=("build", "run"))
