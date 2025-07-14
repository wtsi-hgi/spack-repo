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

	version("1.16.0", commit="d0813fb5c00d72e58bf5c1a7300aef146c047a82")
	version("1.10.0", commit="f96ad1f7259806e48b4da8d9378c6ed577cfe8d7")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-flexmix", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
