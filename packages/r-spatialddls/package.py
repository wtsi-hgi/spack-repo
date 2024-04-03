# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpatialddls(RPackage):
	"""Deconvolution of Spatial Transcriptomics Data Based on Neural
Networks

	Deconvolution of spatial transcriptomics data based on neural networks and single-cell RNA-seq data. SpatialDDLS implements a workflow to create neural network models able to make accurate estimates of cell composition of spots from spatial transcriptomics data using deep learning and the meaningful information provided by single-cell RNA-seq data. See Torroja and Sanchez-Cabo (2019) <doi:10.3389/fgene.2019.00978> and Mañanes et al. (2024) <doi:10.1093/bioinformatics/btae072> to get an overview of the method and see some examples of its performance. 
	"""
	
	homepage = "https://diegommcc.github.io/SpatialDDLS/"
	cran = "SpatialDDLS" 

	version("1.0.1", md5="35dbef7a405944fad91f40acebb29063")

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
