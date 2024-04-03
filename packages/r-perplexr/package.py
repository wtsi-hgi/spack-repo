# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPerplexr(RPackage):
	"""A Coding Assistant using Perplexity's Large Language Models

	A coding assistant using Perplexity's Large Language Models
    <https://www.perplexity.ai/> API. A set of functions and 'RStudio' add-ins
    that aim to help R developers.
	"""
	
	homepage = "https://github.com/GabrielKaiserQFin/perplexR"
	cran = "perplexR" 

	version("0.0.3", md5="669e0b6e7e5524f4556c434aebebc975")

	depends_on("r-clipr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-miniui", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
