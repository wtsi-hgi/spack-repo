# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConsensusde(RPackage):
	"""RNA-seq analysis using multiple algorithms

	This package allows users to perform DE analysis using multiple algorithms. It seeks consensus from multiple methods. Currently it supports "Voom", "EdgeR" and "DESeq". It uses RUV-seq (optional) to remove unwanted sources of variation.
	"""
	
	bioc = "consensusDE" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/consensusDE_1.20.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/consensusDE/consensusDE_1.20.0.tar.gz"]

	version("1.20.0", md5="f4aedcdf9823551d0ea0cc2ae64ac475")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-airway", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dendextend", type=("build", "run"))
	depends_on("r-deseq2@1.20:", type=("build", "run"))
	depends_on("r-edaseq", type=("build", "run"))
	depends_on("r-ensembldb", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-ensdb-hsapiens-v86", type=("build", "run"))
	depends_on("r-genomicalignments", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))
	depends_on("r-pcamethods", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-ruvseq", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-txdb-dmelanogaster-ucsc-dm3-ensgene", type=("build", "run"))
