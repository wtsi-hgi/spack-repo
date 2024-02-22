# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWallace(RPackage):
	"""A Modular Platform for Reproducible Modeling of Species Niches
and Distributions

	The 'shiny' application Wallace is a modular platform for 
    reproducible modeling of species niches and distributions. Wallace
    guides users through a complete analysis, from the acquisition of species
    occurrence and environmental data to visualizing model predictions on an 
    interactive map, thus bundling complex workflows into a single, 
    streamlined interface. An extensive vignette, which guides users through 
    most package functionality can be found on the package's GitHub Pages 
    website: <https://wallaceecomod.github.io/wallace/articles/tutorial-v2.html>.
	"""
	
	homepage = "http://wallaceecomod.github.io/wallace/"
	cran = "wallace" 

	version("2.1.1", md5="2a8a569fa7639204ed8901ba6c71c819")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-shiny@1.6:", type=("build", "run"))
	depends_on("r-leaflet@2.0.2:", type=("build", "run"))
	depends_on("r-dplyr@1.0.2:", type=("build", "run"))
	depends_on("r-dt@0.5:", type=("build", "run"))
	depends_on("r-ecospat@4:", type=("build", "run"))
	depends_on("r-enmeval@2.0.3:", type=("build", "run"))
	depends_on("r-knitcitations", type=("build", "run"))
	depends_on("r-leafem", type=("build", "run"))
	depends_on("r-leaflet-extras@1:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rjava", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-shinyalert", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-shinywidgets@0.6:", type=("build", "run"))
	depends_on("r-spocc@1.2:", type=("build", "run"))
	depends_on("r-spthin", type=("build", "run"))
	depends_on("r-zip", type=("build", "run"))
