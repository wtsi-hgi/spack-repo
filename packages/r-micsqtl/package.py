# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMicsqtl(RPackage):
	"""MICSQTL (Multi-omic deconvolution, Integration and Cell-type-specific Quantitative Trait Loci)

	Our pipeline, MICSQTL, utilizes scRNA-seq reference and bulk transcriptomes to estimate cellular composition in the matched bulk proteomes. The expression of genes and proteins at either bulk level or cell type level can be integrated by Angle-based Joint and Individual Variation Explained (AJIVE) framework. Meanwhile, MICSQTL can perform cell-type-specic quantitative trait loci (QTL) mapping to proteins or transcripts based on the input of bulk expression data and the estimated cellular composition per molecule type, without the need for single cell sequencing. We use matched transcriptome-proteome from human brain frontal cortex tissue samples to demonstrate the input and output of our tool.
	"""
	
	bioc = "MICSQTL"

	version("1.6.0", commit="8d88ac372e5727d896bea0e1cadd093dfb99fa9f")
	version("1.0.0", commit="1494154c1cca4d1f7df2ef13684f05c52cc69f8d")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-tca", type=("build", "run"))
	depends_on("r-nnls", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-toast", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-ggridges", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-dirmult", type=("build", "run"))
