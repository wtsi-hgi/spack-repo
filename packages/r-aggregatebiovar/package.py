# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAggregatebiovar(RPackage):
	"""Differential Gene Expression Analysis for Multi-subject scRNA-seq

	For single cell RNA-seq data collected from more than one subject (e.g. biological sample or technical replicates), this package contains tools to summarize single cell gene expression profiles at the level of subject. A SingleCellExperiment object is taken as input and converted to a list of SummarizedExperiment objects, where each list element corresponds to an assigned cell type. The SummarizedExperiment objects contain aggregate gene-by-subject count matrices and inter-subject column metadata for individual subjects that can be processed using downstream bulk RNA-seq tools.
	"""
	
	homepage = "https://github.com/jasonratcliff/aggregateBioVar"
	bioc = "aggregateBioVar" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/aggregateBioVar_1.12.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/aggregateBioVar/aggregateBioVar_1.12.0.tar.gz"]

	version("1.12.0", sha256="8a165cd344f00c7b07bf45090679f853fdb351b3d33f30ce9590a6cf2c8404c4")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
