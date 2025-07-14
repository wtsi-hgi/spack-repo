# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMiqc(RPackage):
	"""Flexible, probabilistic metrics for quality control of scRNA-seq data

	Single-cell RNA-sequencing (scRNA-seq) has made it possible to profile gene expression in tissues at high resolution.  An important preprocessing step prior to performing downstream analyses is to identify and remove cells with poor or degraded sample quality using quality control (QC) metrics.  Two widely used QC metrics to identify a ‘low-quality’ cell are (i) if the cell includes a high proportion of reads that map to mitochondrial DNA encoded genes (mtDNA) and (ii) if a small number of genes are detected. miQC is data-driven QC metric that jointly models both the proportion of reads mapping to mtDNA and the number of detected genes with mixture models in a probabilistic framework to predict the low-quality cells in a given dataset.
	"""
	
	homepage = "https://github.com/greenelab/miQC"
	bioc = "miQC" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/miQC_1.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/miQC/miQC_1.10.0.tar.gz"]

	version("1.16.0", tag="RELEASE_3_21")
	version("1.10.0", sha256="e089a0972b890bff36cd46d2f02198ddd99911e60bc9a804e964893327b5378c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-flexmix", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
