# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClindatareview(RPackage):
	"""Clinical Data Review Tool

	Creation of interactive tables, listings and figures ('TLFs') 
  and associated report for exploratory analysis of data in a clinical trial, 
  e.g. for clinical oversight activities.
  Interactive figures include sunburst, treemap, scatterplot, line plot and
  barplot of counts data. 
  Interactive tables include table of summary statistics
  (as counts of adverse events, enrollment table) and listings.
  Possibility to compare data (summary table or listing) across two data batches/sets.
  A clinical data review report is created via study-specific configuration 
  files and template 'R Markdown' reports contained in the package.
	"""
	
	homepage = "https://github.com/openanalytics/clinDataReview"
	cran = "clinDataReview" 

	version("1.5.0", md5="151564a3c6daadc5c74dd835cb6e6847")

	depends_on("r-bookdown", type=("build", "run"))
	depends_on("r-clinutils@0.1:", type=("build", "run"))
	depends_on("r-crosstalk", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-haven", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-jsonvalidate", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-xfun", type=("build", "run"))
	depends_on("pandoc", type=("build", "link", "run"))
