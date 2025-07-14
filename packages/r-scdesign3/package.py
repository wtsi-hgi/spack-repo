# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScdesign3(RPackage):
	"""A unified framework of realistic in silico data generation and statistical model inference for single-cell and spatial omics

	We present a statistical simulator, scDesign3, to generate realistic single-cell and spatial omics data, including various cell states, experimental designs, and feature modalities, by learning interpretable parameters from real data. Using a unified probabilistic model for single-cell and spatial omics data, scDesign3 infers biologically meaningful parameters; assesses the goodness-of-fit of inferred cell clusters, trajectories, and spatial locations; and generates in silico negative and positive controls for benchmarking computational tools.
	"""
	
	homepage = "https://github.com/SONGDONGYUAN1994/scDesign3"
	bioc = "scDesign3"

	version("1.6.0", commit="39a5184584635bd04181bdfed6be8257a96d8f8a")
	version("1.0.1", commit="462115d448293163f86198d24bc517b4760839c7")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-gamlss", type=("build", "run"))
	depends_on("r-gamlss-dist", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-pbmcapply", type=("build", "run"))
	depends_on("r-rvinecopulib", type=("build", "run"))
	depends_on("r-umap", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-irlba", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
