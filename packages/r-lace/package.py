# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLace(RPackage):
	"""Longitudinal Analysis of Cancer Evolution (LACE)

	LACE is an algorithmic framework that processes single-cell somatic mutation profiles from cancer samples collected at different time points and in distinct experimental settings, to produce longitudinal models of cancer evolution. The approach solves a Boolean Matrix Factorization problem with phylogenetic constraints, by maximizing a weighed likelihood function computed on multiple time points.
	"""
	
	homepage = "https://github.com/BIMIB-DISCo/LACE"
	bioc = "LACE" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/LACE_2.6.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/LACE/LACE_2.6.1.tar.gz"]

	version("2.6.1", sha256="b82af6d6f2e2581e43a0ede116ab886840f5e34edc59e37a6def9b8f2870bd0b")
	version("2.6.0", md5="d11f64211d10d293c2931b49765b5d61")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-sortable", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-data-tree", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-configr", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-bsplus", type=("build", "run"))
	depends_on("r-shinyvalidate", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinythemes", type=("build", "run"))
	depends_on("r-shinyfiles", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-shinybs", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-biomart", type=("build", "run"))
	depends_on("r-callr", type=("build", "run"))
	depends_on("r-logr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-svglite", type=("build", "run"))
