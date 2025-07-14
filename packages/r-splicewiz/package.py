# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSplicewiz(RPackage):
	"""Easy, optimized, and accurate alternative splicing analysis in R

	The analysis and visualization of alternative splicing (AS) events from RNA sequencing data remains challenging. SpliceWiz is a user-friendly and performance-optimized R package for AS analysis, by processing alignment BAM files to quantify read counts across splice junctions, IRFinder-based intron retention quantitation, and supports novel splicing event identification. We introduce a novel visualization for AS using normalized coverage, thereby allowing visualization of differential AS across conditions. SpliceWiz features a shiny-based GUI facilitating interactive data exploration of results including gene ontology enrichment. It is performance optimized with multi-threaded processing of BAM files and a new COV file format for fast recall of sequencing coverage. Overall, SpliceWiz streamlines AS analysis, enabling reliable identification of functionally relevant AS events for further characterization.
	"""
	
	homepage = "https://github.com/alexchwong/SpliceWiz"
	bioc = "SpliceWiz"

	version("1.10.1", commit="2568ef4483bb5abcd147e4ab1174ab2ea180a5c6")
	version("1.4.1", commit="e98216c7e98a46cf9656a098f522940ce0851ce3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-nxtirfdata", type=("build", "run"))
	depends_on("r-ompbam", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-fst", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-biocfilecache", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-delayedarray", type=("build", "run"))
	depends_on("r-delayedmatrixstats", type=("build", "run"))
	depends_on("r-genefilter", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-hdf5array", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-rhdf5", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinyfiles", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-rhandsontable", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-heatmaply", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-zlibbioc", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
	depends_on("zlib", type=("build", "link", "run"))
