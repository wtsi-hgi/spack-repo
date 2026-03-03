# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSlfm(RPackage):
	"""Fitting a Bayesian Sparse Latent Factor Model in Gene Expression
Analysis

	Set of tools to find coherent patterns in gene expression (microarray) data using a Bayesian Sparse Latent Factor Model (SLFM) <DOI:10.1007/978-3-319-12454-4_15>. Considerable effort has been put to build a fast and memory efficient package, which makes this proposal an interesting and computationally convenient alternative to study patterns of gene expressions exhibited in matrices. The package contains the implementation of two versions of the model based on different mixture priors for the loadings: one relies on a degenerate component at zero and the other uses a small variance normal distribution for the spike part of the mixture. 
	"""
	
	cran = "slfm" 

	version("1.0.2", md5="7ca94fdf39f2ea7ed51a65f2b94b22d3")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
