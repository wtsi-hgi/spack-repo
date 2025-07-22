# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHgc(RPackage):
	"""A fast hierarchical graph-based clustering method

	HGC (short for Hierarchical Graph-based Clustering) is an R package for conducting hierarchical clustering on large-scale single-cell RNA-seq (scRNA-seq) data. The key idea is to construct a dendrogram of cells on their shared nearest neighbor (SNN) graph. HGC provides functions for building graphs and for conducting hierarchical clustering on the graph. The users with old R version could visit https://github.com/XuegongLab/HGC/tree/HGC4oldRVersion to get HGC package built for R 3.6.
	"""
	
	bioc = "HGC" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/HGC_1.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/HGC/HGC_1.10.0.tar.gz"]

	version("1.16.0", tag="RELEASE_3_21")
	version("1.10.0", sha256="c959666b187996788b6d58d9e51c740d942f6e2e58d9fcf4b36602e7450712f5")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rann", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-dendextend", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
