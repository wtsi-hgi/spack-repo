# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSegmenter(RPackage):
	"""Perform Chromatin Segmentation Analysis in R by Calling ChromHMM

	Chromatin segmentation analysis transforms ChIP-seq data into signals over the genome. The latter represents the observed states in a multivariate Markov model to predict the chromatin's underlying states. ChromHMM, written in Java, integrates histone modification datasets to learn the chromatin states de-novo. The goal of this package is to call chromHMM from within R, capture the output files in an S4 object and interface to other relevant Bioconductor analysis tools. In addition, segmenter provides functions to test, select and visualize the output of the segmentation.
	"""
	
	bioc = "segmenter" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/segmenter_1.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/segmenter/segmenter_1.8.0.tar.gz"]

	version("1.8.0", md5="8877dce2f35cc59e9c3d8b3fb38bf29e")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-chipseeker", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-bamsignals", type=("build", "run"))
	depends_on("r-complexheatmap", type=("build", "run"))
	depends_on("r-chromhmmdata", type=("build", "run"))
