# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrapesagri1(RPackage):
	"""Collection of Shiny Apps for Agricultural Research Data Analysis

	Allows user to have graphical user interface to perform analysis of Agricultural experimental data. On using the functions in this package a Interactive User Interface will pop up. Apps Works by simple upload of files in CSV format.
	"""
	
	homepage = "https://github.com/pratheesh3780/grapesAgri1"
	cran = "grapesAgri1" 

	version("1.1.0", md5="bcffd30c65d693babb509120eec1fccc", url="https://cran.r-project.org/src/contrib/grapesAgri1_1.1.0.tar.gz")

	depends_on("r-shiny@1.6:", type=("build", "run"))
	depends_on("r-shinywidgets@0.6:", type=("build", "run"))
	depends_on("r-rmarkdown@2.7:", type=("build", "run"))
	depends_on("r-knitr@1.31:", type=("build", "run"))
	depends_on("r-kableextra@1.3.4:", type=("build", "run"))
	depends_on("r-magrittr@2.0.1:", type=("build", "run"))
	depends_on("r-summarytools@0.9.9:", type=("build", "run"))
	depends_on("r-dplyr@1.0.4:", type=("build", "run"))
	depends_on("r-pastecs@1.3.21:", type=("build", "run"))
	depends_on("r-ggpubr@0.4:", type=("build", "run"))
	depends_on("r-hmisc@4.5:", type=("build", "run"))
	depends_on("r-corrplot@0.84:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.3:", type=("build", "run"))
	depends_on("r-reshape2@1.4.4:", type=("build", "run"))
	depends_on("r-gridgraphics@0.5.1:", type=("build", "run"))
	depends_on("r-rcolorbrewer@1.1.2:", type=("build", "run"))
	depends_on("r-desplot@1.8:", type=("build", "run"))
	depends_on("r-agricolae@1.3.5:", type=("build", "run"))
	depends_on("r-paireddata@1.1.1:", type=("build", "run"))
	depends_on("r-gtools@3.9.2:", type=("build", "run"))
	depends_on("r-rdpack@2.1.2:", type=("build", "run"))
