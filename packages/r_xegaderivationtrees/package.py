# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXegaderivationtrees(RPackage):
	"""Generating and Manipulating Derivation Trees

	Derivation tree operations are needed for implementing 
            grammar-based genetic programming and grammatical evolution:  
            Generating of a random derivation trees of a context-free grammar 
            of bounded depth, decoding a derivation tree, 
            choosing a random node in a derivation tree, 
            extracting a tree whose root is a specified node, and 
            inserting a subtree into a derivation tree at a specified node.
            These operations are necessary for the initializiation and 
            for decoders of a random population of programs, 
            as well as for implementing crossover and mutation operators.
            Depth-bounds are guaranteed by switching to a grammar 
            without recursive production rules. 
            For executing the examples, the package 'BNF' is needed.
            The basic tree operations of generating, extracting, and 
            inserting of derivation trees as well as the conditions 
            for guaranteeing complete derivation trees have been 
            presented in Geyer-Schulz (1997, ISBN:978-3-7908-0830-X).
            The use of random integer vectors for the generation 
            of derivation trees has been introduced in 
            Ryan, C., Collins, J. J., and  O'Neill, M. (1998)
            <doi:10.1007/BFb0055930>. 
	"""
	
	homepage = "<https://github.com/ageyerschulz/xegaDerivationTrees>"
	cran = "xegaDerivationTrees" 

	version("1.0.0.0", md5="2676bee4ce02c2f1a3d7338b96a36be5")

	depends_on("r-xegabnf", type=("build", "run"))
