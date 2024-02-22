# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPowsc(RPackage):
	"""Simulation, power evaluation, and sample size recommendation for single cell RNA-seq

	Determining the sample size for adequate power to detect statistical significance is a crucial step at the design stage for high-throughput experiments. Even though a number of methods and tools are available for sample size calculation for microarray and RNA-seq in the context of differential expression (DE), this topic in the field of single-cell RNA sequencing is understudied. Moreover, the unique data characteristics present in scRNA-seq such as sparsity and heterogeneity increase the challenge. We propose POWSC, a simulation-based method, to provide power evaluation and sample size recommendation for single-cell RNA sequencing DE analysis. POWSC consists of a data simulator that creates realistic expression data, and a power assessor that provides a comprehensive evaluation and visualization of the power and sample size relationship.
	"""
	
	bioc = "POWSC" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/POWSC_1.10.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/POWSC/POWSC_1.10.0.tar.gz"]

	version("1.10.0", md5="e2ed51f94e9a1b37aa91fe74a007f4d7")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-mast", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
