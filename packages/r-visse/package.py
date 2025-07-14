# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVisse(RPackage):
	"""Visualising Set Enrichment Analysis Results

	This package enables the interpretation and analysis of results from a gene set enrichment analysis using network-based and text-mining approaches. Most enrichment analyses result in large lists of significant gene sets that are difficult to interpret. Tools in this package help build a similarity-based network of significant gene sets from a gene set enrichment analysis that can then be investigated for their biological function using text-mining approaches.
	"""
	
	homepage = "https://davislaboratory.github.io/vissE"
	bioc = "vissE" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/vissE_1.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/vissE/vissE_1.10.0.tar.gz"]

    version("1.16.0", tag="RELEASE_3_21")
	version("1.10.0", sha256="041e87a10788ef79fa273d2f1896c24d51fd09dc050fdfd083256670f8e0f0bf")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scico", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-tm", type=("build", "run"))
	depends_on("r-ggwordcloud", type=("build", "run"))
	depends_on("r-gseabase", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-ggforce", type=("build", "run"))
	depends_on("r-msigdb", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-textstem", type=("build", "run"))
	depends_on("r-tidygraph", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-ggraph", type=("build", "run"))
