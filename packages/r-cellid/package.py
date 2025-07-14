# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCellid(RPackage):
	"""Unbiased Extraction of Single Cell gene signatures using Multiple Correspondence Analysis

	CelliD is a clustering-free multivariate statistical method for the robust extraction of per-cell gene signatures from single-cell RNA-seq. CelliD allows unbiased cell identity recognition across different donors, tissues-of-origin, model organisms and single-cell omics protocols. The package can also be used to explore functional pathways enrichment in single cell data.
	"""
	
	bioc = "CelliD" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/CelliD_1.10.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/CelliD/CelliD_1.10.1.tar.gz"]

	version("1.16.0", tag="RELEASE_3_21")
	version("1.10.1", sha256="3bb41e8bac869def13016f2555554dea2a606239f971d4901d1019711bec1c8e")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-seurat@4.0.1:", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-tictoc", type=("build", "run"))
	depends_on("r-scater", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-irlba", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-umap", type=("build", "run"))
	depends_on("r-rtsne", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-fastmatch", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-fgsea", type=("build", "run"))
