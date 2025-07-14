# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSangeranalyser(RPackage):
	"""sangeranalyseR: a suite of functions for the analysis of Sanger sequence data in R

	This package builds on sangerseqR to allow users to create contigs from collections of Sanger sequencing reads. It provides a wide range of options for a number of commonly-performed actions including read trimming, detecting secondary peaks, and detecting indels using a reference sequence. All parameters can be adjusted interactively either in R or in the associated Shiny applications. There is extensive online documentation, and the package can outputs detailed HTML reports, including chromatograms.
	"""
	
	bioc = "sangeranalyseR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/sangeranalyseR_1.12.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/sangeranalyseR/sangeranalyseR_1.12.0.tar.gz"]

	version("1.18.0", tag="RELEASE_3_21")
	version("1.12.0", sha256="25b8ef1292d325dcc71805340ae5b0a628a843b6905307f9e3d101ee9d356935")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-decipher", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-phangorn", type=("build", "run"))
	depends_on("r-sangerseqr", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-zeallot", type=("build", "run"))
	depends_on("r-excelr", type=("build", "run"))
	depends_on("r-shinycssloaders", type=("build", "run"))
	depends_on("r-ggdendro", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-rmarkdown@2.9:", type=("build", "run"))
	depends_on("r-knitr@1.33:", type=("build", "run"))
	depends_on("r-seqinr", type=("build", "run"))
	depends_on("r-biocstyle", type=("build", "run"))
	depends_on("r-logger", type=("build", "run"))
