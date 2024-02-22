# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSleepwalk(RPackage):
	"""Interactively Explore Dimension-Reduced Embeddings

	A tool to interactively explore the
  embeddings created by dimension reduction methods such as 
  Principal Components Analysis (PCA), Multidimensional Scaling (MDS), 
  T-distributed Stochastic Neighbour Embedding (t-SNE),
  Uniform Manifold Approximation and Projection (UMAP) or any other.
	"""
	
	homepage = "https://anders-biostat.github.io/sleepwalk/"
	cran = "sleepwalk" 

	version("0.3.2", md5="a5d66b018eb8d3719b1c5ff51743ec1c")

	depends_on("r-jrc@0.5:", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-httpuv", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
