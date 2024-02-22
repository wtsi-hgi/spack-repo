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
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/CellTrails_1.20.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/CellTrails/CellTrails_1.20.0.tar.gz"]

	version("1.20.0", md5="87b23b653d772f9b436b655e5e8af5ae")

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
