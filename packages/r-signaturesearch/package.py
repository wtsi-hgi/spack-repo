# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSignaturesearch(RPackage):
	"""Environment for Gene Expression Searching Combined with Functional Enrichment Analysis

	This package implements algorithms and data structures for performing gene expression signature (GES) searches, and subsequently interpreting the results functionally with specialized enrichment methods.
	"""
	
	homepage = "https://github.com/yduan004/signatureSearch/"
	bioc = "signatureSearch" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/signatureSearch_1.16.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/signatureSearch/signatureSearch_1.16.0.tar.gz"]

	version("1.16.0", md5="9585172c7764e755ee67aee1c5a1adba")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-hdf5array", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-fgsea", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-qvalue", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-visnetwork", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-fastmatch", type=("build", "run"))
	depends_on("r-reactome-db", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-clusterprofiler", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-dose", type=("build", "run"))
	depends_on("r-rhdf5", type=("build", "run"))
	depends_on("r-gseabase", type=("build", "run"))
	depends_on("r-delayedarray", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
