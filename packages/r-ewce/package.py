# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REwce(RPackage):
	"""Expression Weighted Celltype Enrichment

	Used to determine which cell types are enriched within gene lists. The package provides tools for testing enrichments within simple gene lists (such as human disease associated genes) and those resulting from differential expression studies. The package does not depend upon any particular Single Cell Transcriptome dataset and user defined datasets can be loaded in and used in the analyses.
	"""
	
	homepage = "https://github.com/NathanSkene/EWCE"
	bioc = "EWCE"

	version("1.16.0", commit="fe732b5bd3268b726eb68c92e395c55fc998d271")
	version("1.10.2", commit="0413c77d5ab8586c93a73d2c1b1b2cc0aa78a99d")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-rnomni@1:", type=("build", "run"))
	depends_on("r-ewcedata@1.7.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-hgnchelper", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-delayedarray", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-orthogene@0.99.8:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
