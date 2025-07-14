# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCelltrails(RPackage):
	"""Reconstruction, visualization and analysis of branching trajectories

	CellTrails is an unsupervised algorithm for the de novo chronological ordering, visualization and analysis of single-cell expression data. CellTrails makes use of a geometrically motivated concept of lower-dimensional manifold learning, which exhibits a multitude of virtues that counteract intrinsic noise of single cell data caused by drop-outs, technical variance, and redundancy of predictive variables. CellTrails enables the reconstruction of branching trajectories and provides an intuitive graphical representation of expression patterns along all branches simultaneously. It allows the user to define and infer the expression dynamics of individual and multiple pathways towards distinct phenotypes.
	"""
	
	bioc = "CellTrails"

	version("1.26.0", commit="b49d66cd015647b989d5a14ac03f9ea0391f17a5")
	version("1.20.0", commit="3e1f87c9bd52161511ad0af801297e331cd8ae28")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-cba", type=("build", "run"))
	depends_on("r-dendextend", type=("build", "run"))
	depends_on("r-dtw", type=("build", "run"))
	depends_on("r-envstats", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-maptree", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rtsne", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
