# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMethylscaper(RPackage):
	"""Visualization of Methylation Data

	methylscaper is an R package for processing and visualizing data jointly profiling methylation and chromatin accessibility (MAPit, NOMe-seq, scNMT-seq, nanoNOMe, etc.). The package supports both single-cell and single-molecule data, and a common interface for jointly visualizing both data types through the generation of ordered representational methylation-state matrices. The Shiny app allows for an interactive seriation process of refinement and re-weighting that optimally orders the cells or DNA molecules to discover methylation patterns and nucleosome positioning.
	"""
	
	bioc = "methylscaper" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/methylscaper_1.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/methylscaper/methylscaper_1.10.0.tar.gz"]

	version("1.10.0", md5="0fae72e2aac98ec4a55d8aa4343039ba")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-seriation", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-seqinr", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-shinyfiles", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
