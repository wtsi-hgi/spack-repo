# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeqnet(RPackage):
	"""Generate RNA-Seq Data from Gene-Gene Association Networks

	Methods to generate random gene-gene association networks and simulate RNA-seq data from them, as described in Grimes and Datta (2021) <doi:10.18637/jss.v098.i12>. Includes functions to generate random networks of any size and perturb them to obtain differential networks. Network objects are built from individual, overlapping modules that represent pathways. The resulting network has various topological properties that are characteristic of gene regulatory networks. RNA-seq data can be generated such that the association among gene expression profiles reflect the underlying network. A reference RNA-seq dataset can be provided to model realistic marginal distributions. Plotting functions are available to visualize a network, compare two networks, and compare the expression of two genes across multiple networks.
	"""
	
	cran = "SeqNet" 

	version("1.1.3", md5="a9d79ffb660be9a8dc6e6d3452181c60")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-fitdistrplus", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
