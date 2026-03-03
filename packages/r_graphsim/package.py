# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGraphsim(RPackage):
	"""Simulate Expression Data from 'igraph' Networks

	Functions to develop simulated continuous data (e.g., gene expression) from a sigma covariance matrix derived from a graph structure in 'igraph' objects. Intended to extend 'mvtnorm' to take 'igraph'  structures rather than sigma matrices as input. This allows the use of simulated data that correctly accounts for pathway relationships and correlations. This allows the use of simulated data that correctly accounts for pathway relationships and correlations. Here we present a versatile statistical framework to simulate  correlated gene expression data from biological pathways, by sampling from a multivariate normal distribution derived from a graph structure. This package allows the simulation of biological pathways from a graph structure based on a statistical model of gene expression. For example methods to infer biological pathways and gene regulatory networks from gene expression data can be tested on simulated datasets using this framework. This also allows for pathway structures to be considered as a confounding variable when simulating gene expression data to test the performance of genomic analyses.
	"""
	
	homepage = "https://github.com/TomKellyGenetics/graphsim/"
	cran = "graphsim" 

	version("1.0.3", md5="34208f0964167ef3e8f5c55ce367f79f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
