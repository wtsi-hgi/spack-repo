# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClustifyr(RPackage):
	"""Classifier for Single-cell RNA-seq Using Cell Clusters

	Package designed to aid in classifying cells from single-cell RNA sequencing data using external reference data (e.g., bulk RNA-seq, scRNA-seq, microarray, gene lists). A variety of correlation based methods and gene list enrichment methods are provided to assist cell type assignment.
	"""
	
	homepage = "https://github.com/rnabioco/clustifyr"
	bioc = "clustifyr" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/clustifyr_1.14.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/clustifyr/clustifyr_1.14.0.tar.gz"]

	version("1.14.0", md5="5fc803262c7a3b4d11d464f30a110802")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-entropy", type=("build", "run"))
	depends_on("r-fgsea", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-proxy", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
