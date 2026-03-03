# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetrankr(RPackage):
	"""Analyzing Partial Rankings in Networks

	Implements methods for centrality related analyses of networks. 
    While the package includes the possibility to build more than 20 indices, 
    its main focus lies on index-free assessment of centrality via partial 
    rankings obtained by neighborhood-inclusion or positional dominance. These 
    partial rankings can be analyzed with different methods, including 
    probabilistic methods like computing expected node ranks and relative 
    rank probabilities (how likely is it that a node is more central than another?).
    The methodology is described in depth in the vignettes and in
    Schoch (2018) <doi:10.1016/j.socnet.2017.12.003>.
	"""
	
	homepage = "https://github.com/schochastics/netrankr/"
	cran = "netrankr" 

	version("1.2.3", md5="33b13c65812b4f19bd7d0718750c201d")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-igraph@1.0.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
