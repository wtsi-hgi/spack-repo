# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIntercellar(RPackage):
	"""InterCellar: an R-Shiny app for interactive analysis and exploration of cell-cell communication in single-cell transcriptomics

	InterCellar is implemented as an R/Bioconductor Package containing a Shiny app that allows users to interactively analyze cell-cell communication from scRNA-seq data. Starting from precomputed ligand-receptor interactions, InterCellar provides filtering options, annotations and multiple visualizations to explore clusters, genes and functions. Finally, based on functional annotation from Gene Ontology and pathway databases, InterCellar implements data-driven analyses to investigate cell-cell communication in one or multiple conditions.
	"""
	
	homepage = "https://github.com/martaint/InterCellar"
	bioc = "InterCellar" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/InterCellar_2.8.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/InterCellar/InterCellar_2.8.0.tar.gz"]

	version("2.8.0", md5="a331a8a5f0161dd1e5afa2430660b785")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-config", type=("build", "run"))
	depends_on("r-golem", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-shinyfiles", type=("build", "run"))
	depends_on("r-shinycssloaders", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-colourpicker", type=("build", "run"))
	depends_on("r-dendextend", type=("build", "run"))
	depends_on("r-factoextra", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-shinyfeedback", type=("build", "run"))
	depends_on("r-shinyalert", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-umap", type=("build", "run"))
	depends_on("r-visnetwork", type=("build", "run"))
	depends_on("r-wordcloud2", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-signal", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-complexheatmap", type=("build", "run"))
	depends_on("r-biomart", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-fmsb", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
