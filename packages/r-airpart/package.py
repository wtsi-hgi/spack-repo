# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAirpart(RPackage):
	"""Differential cell-type-specific allelic imbalance

	Airpart identifies sets of genes displaying differential cell-type-specific allelic imbalance across cell types or states, utilizing single-cell allelic counts. It makes use of a generalized fused lasso with binomial observations of allelic counts to partition cell types by their allelic imbalance. Alternatively, a nonparametric method for partitioning cell types is offered. The package includes a number of visualizations and quality control functions for examining single cell allelic imbalance datasets.
	"""
	
	homepage = "https://github.com/Wancen/airpart"
	bioc = "airpart" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/airpart_1.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/airpart/airpart_1.10.0.tar.gz"]

	version("1.10.0", sha256="0b4ff1b2325b5f30d3869faad1330384540ae99b8b053fec5af1528b0e78b4ad")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-scater", type=("build", "run"))
	depends_on("r-smurf", type=("build", "run"))
	depends_on("r-apeglm@1.13.3:", type=("build", "run"))
	depends_on("r-emdbook", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-clue", type=("build", "run"))
	depends_on("r-dynamictreecut", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-complexheatmap", type=("build", "run"))
	depends_on("r-forestplot", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-lpsolve", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
