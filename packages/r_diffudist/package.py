# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiffudist(RPackage):
	"""Diffusion Distance for Complex Networks

	Enables the evaluation of diffusion distances for complex single-layer networks.
    Given a network one can define different types of Laplacian (or transition)
    matrices corresponding to different continuous-time random walks dynamics on the network. 
    This package enables the evaluation of Laplacians, stochastic matrices, and the 
    corresponding diffusion distance matrices. The metric structure induced by the network-driven
    process is richer and more robust than the one given by shortest-paths and allows to study 
    the geometry induced by different types of diffusion-like communication mechanisms taking 
    place on complex networks. 
    For more details see: De Domenico, M. (2017) <doi:10.1103/physrevlett.118.168301> and 
    Bertagnolli, G. and De Domenico, M. (2021) <doi:10.1103/PhysRevE.103.042301>.
	"""
	
	homepage = "https://gbertagnolli.github.io/diffudist/"
	cran = "diffudist" 

	version("1.0.1", md5="cfb688712558c1c5b17c0f09a3a25e5c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
	depends_on("r-ggdendro", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
