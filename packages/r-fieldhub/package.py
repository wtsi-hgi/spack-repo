# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFieldhub(RPackage):
	"""A Shiny App for Design of Experiments in Life Sciences

	A shiny design of experiments (DOE) app that aids in the creation of traditional, 
 un-replicated, augmented and partially-replicated designs applied to agriculture, 
 plant breeding, forestry, animal and biological sciences.
	"""
	
	homepage = "https://github.com/DidierMurilloF/FielDHub"
	cran = "FielDHub" 

	version("1.3.4", md5="c28f0aa750b0246b322c74a0cdd902ce")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-config", type=("build", "run"))
	depends_on("r-golem", type=("build", "run"))
	depends_on("r-shiny@1.7:", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-shinythemes", type=("build", "run"))
	depends_on("r-turner", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-shinyjqui", type=("build", "run"))
	depends_on("r-numbers", type=("build", "run"))
	depends_on("r-blocksdesign", type=("build", "run"))
	depends_on("r-shinycssloaders", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-shinyalert", type=("build", "run"))
	depends_on("r-desplot", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
