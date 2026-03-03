# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTsar(RPackage):
	"""Thermal Shift Analysis in R

	This package automates analysis workflow for Thermal Shift Analysis (TSAS) data. Processing, analyzing, and visualizing data through both shiny applications and command lines. Package aims to simplify data analysis and offer front to end workflow, from raw data to multiple trial analysis.
	"""
	
	bioc = "TSAR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/TSAR_1.0.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/TSAR/TSAR_1.0.0.tar.gz"]

	version("1.0.0", md5="7cc8589151c5b03e247590bbd7dc04dd")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-dplyr@1.0.7:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.5:", type=("build", "run"))
	depends_on("r-ggpubr@0.4:", type=("build", "run"))
	depends_on("r-magrittr@2.0.3:", type=("build", "run"))
	depends_on("r-mgcv@1.8.38:", type=("build", "run"))
	depends_on("r-readxl@1.4:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-tidyr@1.1.4:", type=("build", "run"))
	depends_on("r-shiny@1.7.4.1:", type=("build", "run"))
	depends_on("r-plotly@4.10.2:", type=("build", "run"))
	depends_on("r-shinyjs@2.1:", type=("build", "run"))
	depends_on("r-jsonlite@1.8.7:", type=("build", "run"))
	depends_on("r-rhandsontable@0.3.8:", type=("build", "run"))
	depends_on("r-openxlsx@4.2.5.2:", type=("build", "run"))
	depends_on("r-shinywidgets@0.7.6:", type=("build", "run"))
	depends_on("r-minpack-lm@1.2.3:", type=("build", "run"))
