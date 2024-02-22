# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTrigon(RPackage):
	"""Toolbox for Integrative Pathomics Analysis

	Processing and analysis of pathomics, omics and other medical datasets.
    'tRigon' serves as a toolbox for descriptive and statistical analysis, correlations, 
    plotting and many other methods for exploratory analysis of high-dimensional datasets.
	"""
	
	cran = "tRigon" 

	version("0.3.2", md5="4ce9b600140a5ec142b861d93cb7aae6")

	depends_on("r-boot@1.3.28:", type=("build", "run"))
	depends_on("r-caret@6.0.94:", type=("build", "run"))
	depends_on("r-data-table@1.14.8:", type=("build", "run"))
	depends_on("r-dplyr@1.1.2:", type=("build", "run"))
	depends_on("r-dt@0.28:", type=("build", "run"))
	depends_on("r-factoextra@1.0.7:", type=("build", "run"))
	depends_on("r-ggcorrplot@0.1.4:", type=("build", "run"))
	depends_on("r-ggplot2@3.4.2:", type=("build", "run"))
	depends_on("r-ggpubr@0.6:", type=("build", "run"))
	depends_on("r-ggridges@0.5.4:", type=("build", "run"))
	depends_on("r-markdown@1.7:", type=("build", "run"))
	depends_on("r-patchwork@1.1.2:", type=("build", "run"))
	depends_on("r-randomforest@4.7.1.1:", type=("build", "run"))
	depends_on("r-rcolorbrewer@1.1.3:", type=("build", "run"))
	depends_on("r-readxl@1.4.3:", type=("build", "run"))
	depends_on("r-sessioninfo@1.2.2:", type=("build", "run"))
	depends_on("r-shiny@1.7.4.1:", type=("build", "run"))
	depends_on("r-shinydashboardplus@2.0.3:", type=("build", "run"))
	depends_on("r-shinydashboard@0.7.2:", type=("build", "run"))
	depends_on("r-shinywidgets@0.7.6:", type=("build", "run"))
	depends_on("r-simpleboot@1.1.7:", type=("build", "run"))
	depends_on("r-writexl@1.4.2:", type=("build", "run"))
