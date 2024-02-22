# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMonographar(RPackage):
	"""Taxonomic Monographs Tools

	Contains functions intended to facilitate the production of plant taxonomic monographs. The package includes functions to convert tables into taxonomic descriptions, lists of collectors, examined specimens, identification keys (dichotomous and interactive), and can generate a monograph skeleton. Additionally, wrapper functions to batch the production of phenology histograms and distributional and diversity maps are also available.
	"""
	
	cran = "monographaR" 

	version("1.3.1", md5="dce243d210d31dc695c0d030d866fd39")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-circular", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-rnaturalearth", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-shinythemes", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
