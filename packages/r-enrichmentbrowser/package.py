# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REnrichmentbrowser(RPackage):
	"""Seamless navigation through combined results of set-based and network-based enrichment analysis

	The EnrichmentBrowser package implements essential functionality for the enrichment analysis of gene expression data. The analysis combines the advantages of set-based and network-based enrichment analysis in order to derive high-confidence gene sets and biological pathways that are differentially regulated in the expression data under investigation. Besides, the package facilitates the visualization and exploration of such sets and pathways.
	"""
	
	bioc = "EnrichmentBrowser" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/EnrichmentBrowser_2.32.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/EnrichmentBrowser/EnrichmentBrowser_2.32.0.tar.gz"]

	version("2.32.0", sha256="04fb60496346ee2a404c655b807db9a06fd289f4090ddc16f4ba6b78133573d3")

	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-biocfilecache", type=("build", "run"))
	depends_on("r-biocmanager", type=("build", "run"))
	depends_on("r-gseabase", type=("build", "run"))
	depends_on("r-go-db", type=("build", "run"))
	depends_on("r-keggrest", type=("build", "run"))
	depends_on("r-kegggraph", type=("build", "run"))
	depends_on("r-rgraphviz", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-spia", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-graphite", type=("build", "run"))
	depends_on("r-hwriter", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-pathview", type=("build", "run"))
	depends_on("r-safe", type=("build", "run"))
