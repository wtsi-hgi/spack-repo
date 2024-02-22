# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTfrmtbuilder(RPackage):
	"""'shiny' App Companion to the 'tfrmt' Package

	Provides an interactive interface to the 'tfrmt' package. Users 
    can import, modify, and export tables and templates with little to no code. 
	"""
	
	homepage = "https://gsk-biostatistics.github.io/tfrmtbuilder/"
	cran = "tfrmtbuilder" 

	version("0.0.5", md5="61eca692aa9b9dc9ff2750e49d764ada")

	depends_on("r-tfrmt@0.1:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-gt", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sortable", type=("build", "run"))
	depends_on("r-bslib", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-rio", type=("build", "run"))
	depends_on("r-shinycssloaders", type=("build", "run"))
	depends_on("r-webshot2", type=("build", "run"))
	depends_on("r-shinyace", type=("build", "run"))
	depends_on("r-shinyfeedback", type=("build", "run"))
	depends_on("r-fontawesome", type=("build", "run"))
