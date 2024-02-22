# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeahors(RPackage):
	"""Spatial Exploration of ArcHaeological Objects in R Shiny

	An R 'Shiny' application dedicated to the intra-site spatial analysis of piece-plotted archaeological remains, making the two and three-dimensional spatial exploration of archaeological data as user-friendly as possible.  Documentation about 'SEAHORS' is provided by the vignette included in this package and by the companion scientific paper: Royer, Discamps, Plutniak, Thomas (2023, PCI Archaeology, <doi:10.5281/zenodo.7674698>).
	"""
	
	homepage = "https://github.com/AurelienRoyer/SEAHORS"
	cran = "SEAHORS" 

	version("1.8.0", md5="452158395e04ace6b36d66ecab28b828")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinythemes", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
