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

	version("1.16.0", commit="5e19230d8e727e6386e6cc12e41424ba76325d3b")
	version("1.10.0", commit="7666c3b98f96f51ae8c998b65e8857476ba9322d")

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
