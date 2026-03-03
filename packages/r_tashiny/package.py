# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTashiny(RPackage):
	"""'Text Analyzer Shiny'

	Interactive shiny application for working with textmining and text analytics. Various visualizations  are provided.
	"""
	
	cran = "TAShiny" 

	version("0.1.0", md5="223a3adae7ff2d0bc7f962ef3fa950ea")

	depends_on("r@3.0.3:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-tm", type=("build", "run"))
	depends_on("r-snowballc", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-wordcloud2", type=("build", "run"))
