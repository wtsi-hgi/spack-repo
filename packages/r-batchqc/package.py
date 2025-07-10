# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBatchqc(RPackage):
	"""Batch Effects Quality Control Software

	Sequencing and microarray samples often are collected or processed in multiple batches or at different times. This often produces technical biases that can lead to incorrect results in the downstream analysis. BatchQC is a software tool that streamlines batch preprocessing and evaluation by providing interactive diagnostics, visualizations, and statistical analyses to explore the extent to which batch variation impacts the data. BatchQC diagnostics help determine whether batch adjustment needs to be done, and how correction should be applied before proceeding with a downstream analysis. Moreover, BatchQC interactively applies multiple common batch effect approaches to the data, and the user can quickly see the benefits of each method. BatchQC is developed as a Shiny App. The output is organized into multiple tabs, and each tab features an important part of the batch effect analysis and visualization of the data. The BatchQC interface has the following analysis groups: Summary, Differential Expression, Median Correlations, Heatmaps, Circular Dendrogram, PCA Analysis, Shape, ComBat and SVA.
	"""
	
	homepage = "https://github.com/mani2012/BatchQC"
	bioc = "BatchQC" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/BatchQC_1.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/BatchQC/BatchQC_1.30.0.tar.gz"]

	version("1.30.0", sha256="d89b36b950e87c4c7ae7e28d91fa997497b07a500eec85a8907f9f25c623caf5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-pander", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-mcmcpack", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-sva", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-moments", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-ggvis", type=("build", "run"))
	depends_on("r-heatmaply", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("pandoc", type=("build", "link", "run"))
