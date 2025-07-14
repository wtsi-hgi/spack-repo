# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSgcp(RPackage):
	"""SGCP: A semi-supervised pipeline for gene clustering using self-training approach in gene co-expression networks

	SGC is a semi-supervised pipeline for gene clustering in gene co-expression networks. SGC consists of multiple novel steps that enable the computation of highly enriched modules in an unsupervised manner. But unlike all existing frameworks, it further incorporates a novel step that leverages Gene Ontology information in a semi-supervised clustering method that further improves the quality of the computed modules.
	"""
	
	homepage = "https://github.com/na396/SGCP"
	bioc = "SGCP" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/SGCP_1.2.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/SGCP/SGCP_1.2.0.tar.gz"]

    version("1.8.0", tag="RELEASE_3_21")
	version("1.2.0", sha256="4a6a5196e9cd4bba67b5488740cfacb2c1b8e013762c96a31d679dc3615e80b1")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-go-db", type=("build", "run"))
	depends_on("r-annotate", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-genefilter", type=("build", "run"))
	depends_on("r-gostats", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-rgraphviz", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-ggridges", type=("build", "run"))
	depends_on("r-desctools", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
