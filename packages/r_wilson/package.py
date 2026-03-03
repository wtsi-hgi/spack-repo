# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWilson(RPackage):
	"""Web-Based Interactive Omics Visualization

	Tool-set of modules for creating web-based applications that use plot based strategies to visualize and analyze multi-omics data.
    This package utilizes the 'shiny' and 'plotly' frameworks to provide a user friendly dashboard for interactive plotting.
	"""
	
	homepage = "https://github.com/loosolab/wilson/"
	cran = "wilson" 

	version("2.4.2", md5="17bbf112ad07800632b442bcc0a729bd")

	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plotly@4.8:", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-dt@0.3:", type=("build", "run"))
	depends_on("r-colourpicker", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-rje", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-complexheatmap", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-rintrojs", type=("build", "run"))
	depends_on("r-rjsonio", type=("build", "run"))
	depends_on("r-ggrepel@0.6.12:", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-factominer", type=("build", "run"))
	depends_on("r-factoextra", type=("build", "run"))
	depends_on("r-heatmaply@0.14.1:", type=("build", "run"))
	depends_on("r-shinycssloaders", type=("build", "run"))
	depends_on("r-log4r", type=("build", "run"))
	depends_on("r-openssl", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-zip", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
