# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGseabenchmarker(RPackage):
	"""Reproducible GSEA Benchmarking

	The GSEABenchmarkeR package implements an extendable framework for reproducible evaluation of set- and network-based methods for enrichment analysis of gene expression data. This includes support for the efficient execution of these methods on comprehensive real data compendia (microarray and RNA-seq) using parallel computation on standard workstations and institutional computer grids. Methods can then be assessed with respect to runtime, statistical significance, and relevance of the results for the phenotypes investigated.
	"""
	
	homepage = "https://github.com/waldronlab/GSEABenchmarkeR"
	bioc = "GSEABenchmarkeR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/GSEABenchmarkeR_1.22.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/GSEABenchmarkeR/GSEABenchmarkeR_1.22.0.tar.gz"]

	version("1.28.1", tag="RELEASE_3_21")
	version("1.22.0", sha256="0fb82b3b0679fea1fe291390680452401eced6afba91575d488fb9aaf021e191")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-biocfilecache", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-enrichmentbrowser", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-keggandmetacoredzpathwaysgeo", type=("build", "run"))
	depends_on("r-keggdzpathwaysgeo", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
