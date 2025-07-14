# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNanomethviz(RPackage):
	"""Visualise methlation data from Oxford Nanopore sequencing

	NanoMethViz is a toolkit for visualising methylation data from Oxford Nanopore sequencing. It can be used to explore methylation patterns from reads derived from Oxford Nanopore direct DNA sequencing with methylation called by callers including nanopolish, f5c and megalodon. The plots in this package allow the visualisation of methylation profiles aggregated over experimental groups and across classes of genomic features.
	"""
	
	homepage = "https://github.com/shians/NanoMethViz"
	bioc = "NanoMethViz"

	version("3.4.0", commit="855d22b0a23014607369e3de5de01cc3420f6e9c")
	version("2.8.1", commit="1d8a14942ebf7e6ad98855a451826d8f08a0affa")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-cpp11@0.2.5:", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-biocsingular", type=("build", "run"))
	depends_on("r-bsseq", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dbscan", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-ggrastr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-limma@3.44:", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-scales@1.2:", type=("build", "run"))
	depends_on("r-scico", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-zlibbioc", type=("build", "run"))
	depends_on("zlib", type=("build", "link", "run"))
