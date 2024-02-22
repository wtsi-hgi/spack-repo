# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSfs(RPackage):
	"""Similarity-First Search Seriation Algorithm

	An implementation of the Similarity-First Search algorithm (SFS), a combinatorial algorithm which can be used to solve the seriation problem and to recognize some structured weighted graphs. The SFS algorithm represents a generalization to weighted graphs of the graph search algorithm Lexicographic Breadth-First Search (Lex-BFS), a variant of Breadth-First Search. The SFS algorithm reduces to Lex-BFS when applied to binary matrices (or, equivalently, unweighted graphs). Hence this library can be also considered for Lex-BFS applications such as recognition of graph classes like chordal or unit interval graphs. In fact, the SFS seriation algorithm implemented in this package is a multisweep algorithm, which consists in repeating a finite number of SFS iterations (at most n sweeps for a matrix of size n). If the data matrix has a Robinsonian structure, then the ranking returned by the multistep SFS algorithm is a Robinson ordering of the input matrix. Otherwise the algorithm can be used as a heuristic to return a ranking partially satisfying the Robinson property. 
	"""
	
	cran = "SFS" 

	version("0.1.4", md5="98e459b73030529990000aa2ac6a939d")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
