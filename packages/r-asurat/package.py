# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAsurat(RPackage):
	"""Functional annotation-driven unsupervised clustering for single-cell data

	ASURAT is a software for single-cell data analysis. Using ASURAT, one can simultaneously perform unsupervised clustering and biological interpretation in terms of cell type, disease, biological process, and signaling pathway activity. Inputting a single-cell RNA-seq data and knowledge-based databases, such as Cell Ontology, Gene Ontology, KEGG, etc., ASURAT transforms gene expression tables into original multivariate tables, termed sign-by-sample matrices (SSMs).
	"""
	
	bioc = "ASURAT" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/ASURAT_1.6.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/ASURAT/ASURAT_1.6.0.tar.gz"]

	version("1.6.0", md5="a1cb615f6ddab8cb8b9ccb1a73ba39de")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-plot3d", type=("build", "run"))
	depends_on("r-complexheatmap", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
