# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProlocgui(RPackage):
	"""Interactive visualisation of spatial proteomics data

	The package pRolocGUI comprises functions to interactively visualise spatial proteomics data on the basis of pRoloc, pRolocdata and shiny.
	"""
	
	homepage = "https://github.com/lgatto/pRolocGUI"
	bioc = "pRolocGUI" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/pRolocGUI_2.12.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/pRolocGUI/pRolocGUI_2.12.0.tar.gz"]

	version("2.12.0", md5="a9947bbed5501a1c2c68f7c35364c1da")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-proloc@1.27.6:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-msnbase@2.1.11:", type=("build", "run"))
	depends_on("r-shiny@0.9.1:", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dt@0.1.40:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-shinydashboardplus@2:", type=("build", "run"))
	depends_on("r-colourpicker", type=("build", "run"))
	depends_on("r-shinyhelper", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
