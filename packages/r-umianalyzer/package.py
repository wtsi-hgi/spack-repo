# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUmianalyzer(RPackage):
	"""Tools for Analyzing Sequencing Data with Unique Molecular
Identifiers

	Tools for analyzing sequencing data containing unique
    molecular identifiers generated by 'UMIErrorCorrect'
    (<https://github.com/stahlberggroup/umierrorcorrect>).
	"""
	
	homepage = "https://github.com/sfilges/umiAnalyzer"
	cran = "umiAnalyzer" 

	version("1.0.0", md5="54b79eda06469dfaa58b8c73cf6afacd")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-biocmanager", type=("build", "run"))
	depends_on("r-dplyr@0.7.5:", type=("build", "run"))
	depends_on("r-dt@0.19:", type=("build", "run"))
	depends_on("r-forcats@0.5:", type=("build", "run"))
	depends_on("r-ggplot2@2.2.1:", type=("build", "run"))
	depends_on("r-gridextra@2.3:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-pheatmap@1.0.12:", type=("build", "run"))
	depends_on("r-plotly@4.9.2.1:", type=("build", "run"))
	depends_on("r-readr@1.1.1:", type=("build", "run"))
	depends_on("r-rsamtools@1.32.3:", type=("build", "run"))
	depends_on("r-scales@1.1:", type=("build", "run"))
	depends_on("r-shiny@1.7.1:", type=("build", "run"))
	depends_on("r-shinydashboard@0.7.2:", type=("build", "run"))
	depends_on("r-shinyfiles@0.9:", type=("build", "run"))
	depends_on("r-shinywidgets@0.6.2:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-tibble@1.4.2:", type=("build", "run"))
	depends_on("r-tidyr@0.8.1:", type=("build", "run"))
	depends_on("r-viridis@0.5.1:", type=("build", "run"))
