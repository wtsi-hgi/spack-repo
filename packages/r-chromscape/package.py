# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChromscape(RPackage):
	"""Analysis of single-cell epigenomics datasets with a Shiny App

	ChromSCape - Chromatin landscape profiling for Single Cells - is a ready-to-launch user-friendly Shiny Application for the analysis of single-cell epigenomics datasets (scChIP-seq, scATAC-seq, scCUT&Tag, ...) from aligned data to differential analysis & gene set enrichment analysis. It is highly interactive, enables users to save their analysis and covers a wide range of analytical steps: QC, preprocessing, filtering, batch correction, dimensionality reduction, vizualisation, clustering, differential analysis and gene set analysis.
	"""
	
	homepage = "https://github.com/vallotlab/ChromSCape"
	bioc = "ChromSCape" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ChromSCape_1.12.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ChromSCape/ChromSCape_1.12.0.tar.gz"]

	version("1.12.0", sha256="74e00d0ef885ae9bad35823b8158c821714cfe362e4ad6112c20740af518f8b1")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-colourpicker", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-shinyfiles", type=("build", "run"))
	depends_on("r-shinyhelper", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-shinydashboardplus", type=("build", "run"))
	depends_on("r-shinycssloaders", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-colorramps", type=("build", "run"))
	depends_on("r-kableextra", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-batchelor", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-gggenes", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-qualv", type=("build", "run"))
	depends_on("r-stringdist", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-qs", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-scran", type=("build", "run"))
	depends_on("r-scater", type=("build", "run"))
	depends_on("r-consensusclusterplus", type=("build", "run"))
	depends_on("r-rtsne", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-irlba", type=("build", "run"))
	depends_on("r-rlist", type=("build", "run"))
	depends_on("r-umap", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-msigdbr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-coop", type=("build", "run"))
	depends_on("r-matrixtests", type=("build", "run"))
	depends_on("r-delayedarray", type=("build", "run"))
