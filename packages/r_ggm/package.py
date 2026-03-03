# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgm(RPackage):
	"""Graphical Markov Models with Mixed Graphs

	Provides functions for defining 
    mixed graphs containing three types of edges, directed, 
    undirected and bi-directed, with possibly multiple edges.
    These graphs are useful because they capture fundamental
    independence structures in multivariate distributions
    and in the induced distributions after marginalization 
    and conditioning.
    The package is especially concerned with Gaussian graphical
    models for
    (i) ML estimation for directed acyclic graphs, undirected and 
    bi-directed graphs and ancestral graph models
    (ii) testing several conditional independencies
    (iii) checking global identification of DAG Gaussian models
    with one latent variable
    (iv) testing Markov equivalences and generating Markov 
    equivalent graphs of specific types.
	"""
	
	homepage = "https://github.com/StaThin/ggm"
	cran = "ggm" 

	version("2.5.1", md5="db8c249f2c58705be639f0757e9dfaad")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-biocmanager", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
