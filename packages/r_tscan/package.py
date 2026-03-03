# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTscan(RPackage):
	"""Tools for Single-Cell Analysis

	Provides methods to perform trajectory analysis based on a minimum spanning tree constructed from cluster centroids. Computes pseudotemporal cell orderings by mapping cells in each cluster (or new cells) to the closest edge in the tree. Uses linear modelling to identify differentially expressed genes along each path through the tree. Several plotting and interactive visualization functions are also implemented.
	"""
	
	bioc = "TSCAN" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/TSCAN_1.40.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/TSCAN/TSCAN_1.40.1.tar.gz"]

	version("1.40.1", md5="8ab1f3f5a68c4aa03e7e7ed10c61a20f")

	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-trajectoryutils", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-fastica", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-combinat", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-delayedarray", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
