# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXegagpgene(RPackage):
	"""Genetic Operations for Grammar-Based Genetic Programming

	An implementation of
        the representation-dependent gene level operations of grammar-based
        genetic programming with genes which are derivation trees
        of a context-free grammar: Initialization of a gene with a 
        complete random derivation tree, decoding of a derivation tree.
        Crossover is implemented by exchanging subtrees. Depth-bounds
        for the minimal and the maximal depth of the roots of the subtrees
        exchanged by crossover can be set. 
        Mutation is implemented by replacing a subtree by a random subtree. 
        The depth of the random subtree and the insertion node are 
        configurable. For details, 
        see Geyer-Schulz (1997, ISBN:978-3-7908-0830-X).
	"""
	
	homepage = "<https://github.com/ageyerschulz/xegaGpGene>"
	cran = "xegaGpGene" 

	version("1.0.0.0", md5="32d499b2af352edb24a2f88baecfe2b6")

	depends_on("r-xegabnf", type=("build", "run"))
	depends_on("r-xegaderivationtrees", type=("build", "run"))
	depends_on("r-xegaselectgene", type=("build", "run"))
