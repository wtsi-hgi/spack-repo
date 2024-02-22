# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTsviz(RPackage):
	"""Easy and Interactive Time Series Visualization

	An 'RStudio' add-in to visualize time series. Time series are searched in the global environment as data.frame objects with a column of type date and a column of type numeric. Interactive charts are produced using 'plotly' package.
	"""
	
	homepage = "https://github.com/donlelef/tsviz"
	cran = "tsviz" 

	version("0.1.0", md5="96639d8fa75c4dd0b4c9024d590d3b10")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr@0.8:", type=("build", "run"))
	depends_on("r-lubridate@1.7:", type=("build", "run"))
	depends_on("r-plotly@4.9:", type=("build", "run"))
	depends_on("r-shiny@1.2:", type=("build", "run"))
	depends_on("r-miniui@0.1.1:", type=("build", "run"))
	depends_on("r-forecast@8.7:", type=("build", "run"))
	depends_on("r-ggplot2@3:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-shinyhelper@0.3.1:", type=("build", "run"))
