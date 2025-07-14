# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPigengene(RPackage):
	"""Infers biological signatures from gene expression data

	Pigengene package provides an efficient way to infer biological signatures from gene expression profiles. The signatures are independent from the underlying platform, e.g., the input can be microarray or RNA Seq data. It can even infer the signatures using data from one platform, and evaluate them on the other. Pigengene identifies the modules (clusters) of highly coexpressed genes using coexpression network analysis, summarizes the biological information of each module in an eigengene, learns a Bayesian network that models the probabilistic dependencies between modules, and builds a decision tree based on the expression of eigengenes.
	"""
	
	bioc = "Pigengene" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Pigengene_1.28.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/Pigengene/Pigengene_1.28.0.tar.gz"]

	version("1.34.0", tag="RELEASE_3_21")
	version("1.28.0", sha256="7375a0be2eb648a6442ecbc6f29795c6fbce303402c0dd2e6c8f79d2b1c1096a")

	depends_on("r@4.0.3:", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-biocstyle@2.28:", type=("build", "run"))
	depends_on("r-bnlearn@4.7:", type=("build", "run"))
	depends_on("r-c50@0.1.2:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-partykit", type=("build", "run"))
	depends_on("r-rgraphviz", type=("build", "run"))
	depends_on("r-wgcna", type=("build", "run"))
	depends_on("r-go-db", type=("build", "run"))
	depends_on("r-impute", type=("build", "run"))
	depends_on("r-preprocesscore", type=("build", "run"))
	depends_on("r-pheatmap@1.0.8:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-gdata", type=("build", "run"))
	depends_on("r-clusterprofiler", type=("build", "run"))
	depends_on("r-reactomepa", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-dose", type=("build", "run"))
