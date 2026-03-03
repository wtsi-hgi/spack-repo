# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBaycn(RPackage):
	"""Bayesian Inference for Causal Networks

	A Bayesian hybrid approach for inferring Directed Acyclic Graphs
    (DAGs) for continuous, discrete, and mixed data. The algorithm can use the 
    graph inferred by another more efficient graph inference method as input;
    the input graph may contain false edges or undirected edges but can help
    reduce the search space to a more manageable size. A Bayesian Markov chain
    Monte Carlo algorithm is then used to infer the probability of direction and
    absence for the edges in the network.
    References:
    Martin and Fu (2019) <arXiv:1909.10678>.
	"""
	
	cran = "baycn" 

	version("1.2.0", md5="a7c65079f5d293385871c94369d10580")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-egg", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
