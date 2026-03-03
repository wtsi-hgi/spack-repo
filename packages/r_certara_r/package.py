# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCertaraR(RPackage):
	"""Easily Install Pharmacometric Packages and Shiny Applications
Developed by Certara

	A convenient set of wrapper functions to install
    pharmacometric packages and Shiny applications developed by Certara
    PMX and Integrated Drug Development (iDD). The functions ensure the
    successful installation of packages from non-standard repositories.
	"""
	
	homepage = "https://github.com/certara/R-Certara"
	cran = "Certara.R" 

	version("1.1.0", md5="2dfa5944055545856c4c70f63d9605bd")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-batchtools@0.9.9:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-remotes", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-shinymaterial", type=("build", "run"))
	depends_on("r-shinyjqui", type=("build", "run"))
	depends_on("r-sortable", type=("build", "run"))
	depends_on("r-ssh", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
