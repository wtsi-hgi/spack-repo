# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRamcharts4(RPackage):
	"""Interface to the JavaScript Library 'amCharts 4'

	Creates JavaScript charts. The charts can be included in 'Shiny' apps and R markdown documents, or viewed from the R console and 'RStudio' viewer. Based on the JavaScript library 'amCharts 4' and the R packages 'htmlwidgets' and 'reactR'. Currently available types of chart are: vertical and horizontal bar chart, radial bar chart, stacked bar chart, vertical and horizontal Dumbbell chart, line chart, scatter chart, range area chart, gauge chart, boxplot chart, pie chart, and 100% stacked bar chart.
	"""
	
	homepage = "https://github.com/stla/rAmCharts4"
	cran = "rAmCharts4" 

	version("1.6.0", md5="1a9aa36c4287a4ce9bf768f4cd9b8965", url="https://cran.r-project.org/src/contrib/rAmCharts4_1.6.0.tar.gz")

	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-htmlwidgets@1.5.3:", type=("build", "run"))
	depends_on("r-reactr", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
