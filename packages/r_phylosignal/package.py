# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhylosignal(RPackage):
	"""Exploring the Phylogenetic Signal in Continuous Traits

	A collection of tools to explore the phylogenetic signal in univariate and multivariate data. The package provides functions to plot traits data against a phylogenetic tree, different measures and tests for the phylogenetic signal, methods to describe where the signal is located and a phylogenetic clustering method.
	"""
	
	cran = "phylosignal" 

	version("1.3.1", md5="ad8a22ed62da74d562554d452ef99037")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-adephylo", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-phylobase", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
