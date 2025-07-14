# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCorral(RPackage):
	"""Correspondence Analysis for Single Cell Data

	Correspondence analysis (CA) is a matrix factorization method, and is similar to principal components analysis (PCA). Whereas PCA is designed for application to continuous, approximately normally distributed data, CA is appropriate for non-negative, count-based data that are in the same additive scale. The corral package implements CA for dimensionality reduction of a single matrix of single-cell data, as well as a multi-table adaptation of CA that leverages data-optimized scaling to align data generated from different sequencing platforms by projecting into a shared latent space. corral utilizes sparse matrices and a fast implementation of SVD, and can be called directly on Bioconductor objects (e.g., SingleCellExperiment) for easy pipeline integration. The package also includes additional options, including variations of CA to address overdispersion in count data (e.g., Freeman-Tukey chi-squared residual), as well as the option to apply CA-style processing to continuous data (e.g., proteomic TOF intensities) with the Hellinger distance adaptation of CA.
	"""
	
	bioc = "corral" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/corral_1.12.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/corral/corral_1.12.0.tar.gz"]

    version("1.18.0", tag="RELEASE_3_21")
	version("1.12.0", sha256="6c5dfd037fd9cf6f83eab84fc62cca07c0464a00e00061d838a33b9553cb9348")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggthemes", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-irlba", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-multiassayexperiment", type=("build", "run"))
	depends_on("r-pals", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-transport", type=("build", "run"))
