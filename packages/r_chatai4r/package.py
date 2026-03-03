# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChatai4r(RPackage):
	"""Chat-Based Interactive Artificial Intelligence for R

	The Large Language Model (LLM) represents a groundbreaking advancement 
    in data science and programming, and also allows us to extend the world of R. 
    A seamless interface for integrating the 'OpenAI' Web APIs into R is provided in this package. 
    This package leverages LLM-based AI techniques, enabling efficient knowledge discovery and data analysis 
    (see 'OpenAI' Web APIs details <https://openai.com/blog/openai-api>).
    The previous functions such as seamless translation and image generation have been moved 
    to other packages 'deepRstudio' and 'stableDiffusion4R'.
	"""
	
	homepage = "https://kumes.github.io/chatAI4R/"
	cran = "chatAI4R" 

	version("0.2.10", md5="d6c155d00c0ae474e55811f41bd070f8")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-clipr", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-deeprstudio", type=("build", "run"))
	depends_on("r-pdftools", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
