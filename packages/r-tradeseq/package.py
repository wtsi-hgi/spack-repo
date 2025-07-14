# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTradeseq(RPackage):
	"""trajectory-based differential expression analysis for sequencing data

	tradeSeq provides a flexible method for fitting regression models that can be used to find genes that are differentially expressed along one or multiple lineages in a trajectory. Based on the fitted models, it uses a variety of tests suited to answer different questions of interest, e.g. the discovery of genes for which expression is associated with pseudotime, or which are differentially expressed (in a specific region) along the trajectory. It fits a negative binomial generalized additive model (GAM) for each gene, and performs inference on the parameters of the GAM.
	"""
	
	homepage = "https://statomics.github.io/tradeSeq/index.html"
	bioc = "tradeSeq"

	version("1.22.0", commit="e8f3144dfee5d77d48552929e33b8d490fa0b38c")
	version("1.16.0", commit="aa847e727b2dbf319c72f1df2f56eef790161e27")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-slingshot", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-princurve", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-trajectoryutils", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
