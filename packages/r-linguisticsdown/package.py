# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLinguisticsdown(RPackage):
	"""Easy Linguistics Document Writing with R Markdown

	Provides 'Shiny gadgets' to search, type, and insert IPA symbols
    into documents or scripts, requiring only knowledge about phonetics or 
    'X-SAMPA'. Also provides functions to facilitate the rendering of IPA
    symbols in 'LaTeX' and PDF format, making IPA symbols properly rendered
    in all output formats. A minimal R Markdown template for authoring 
    Linguistics related documents is also bundled with the package. Some
    helper functions to facilitate authoring with R Markdown is also provided.
	"""
	
	homepage = "https://liao961120.github.io/linguisticsdown/"
	cran = "linguisticsdown" 

	version("1.2.0", md5="f600aef666a06e32fa1d4808c91ac3f4")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-miniui", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
