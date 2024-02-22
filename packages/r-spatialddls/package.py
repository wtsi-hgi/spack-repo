# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpatialddls(RPackage):
	"""Deconvolution of Spatial Transcriptomics Data Based on Neural
Networks

	Deconvolution of spatial transcriptomics data using deconvolution models based on deep neural networks and single-cell RNA-seq data. These models are able to make accurate estimates of the cell composition of spots in spatial transcriptomics datasets from the same context using the advances provided by deep learning and the meaningful information provided by single-cell RNA-Seq data. See Torroja and Sanchez-Cabo (2019) <doi:10.3389/fgene.2019.00978> and Mañanes et al. (2023) <doi:10.1101/2023.08.31.555677> to get an overview of the method and see some examples of its performance. 
	"""
	
	homepage = "https://diegommcc.github.io/SpatialDDLS/"
	cran = "SpatialDDLS" 

	version("1.0.0", md5="8c8f68521d5aab50dc27bca777b3731a")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-grr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-spatialexperiment", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-zinbwave", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-keras", type=("build", "run"))
	depends_on("r-tensorflow", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-scran", type=("build", "run"))
	depends_on("r-scuttle", type=("build", "run"))
	depends_on("python@2.7.0:", type=("build", "link", "run"))
	depends_on("py-tensorflow", type=("build", "link", "run"))
