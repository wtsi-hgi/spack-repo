# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLoonShiny(RPackage):
	"""Automatically Create a 'Shiny' App Based on Interactive 'Loon'
Widgets

	Package 'shiny' provides interactive web applications in R. Package 'loon' is an interactive toolkit engaged in open-ended, creative and unscripted data exploration. The 'loon.shiny' package can take 'loon' widgets and display a selfsame 'shiny' app. 
	"""
	
	cran = "loon.shiny" 

	version("1.0.3", md5="5ee76ce33c0199bebbee0266148a4e39")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-loon@1.3.7:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-loon-ggplot@1.1:", type=("build", "run"))
	depends_on("r-colourpicker", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
