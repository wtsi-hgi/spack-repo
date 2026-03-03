# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXegapermgene(RPackage):
	"""Operations on Permutation Genes

	An implementation of 
        representation-dependent gene level operations for
        genetic algorithms with genes which represent permutations: 
        initialization of genes, mutation and crossover.
        The crossover operation provided is position-based crossover 
        (Syswerda, G., Chap. 21 in Davis, L. (1991, ISBN:0-442-00173-8). 
        For mutation, several variants are included: Order-based mutation
        (Syswerda, G., Chap. 21 in Davis, L. (1991, ISBN:0-442-00173-8), 
        randomized Lin-Kernighan heuristics
        (Croes, G. A. (1958) <doi:10.1287/opre.6.6.791> and
         Lin, S. and Kernighan. B. W. (1973) 
        <doi:10.1287/opre.21.2.498>), 
        and randomized greedy operators.
        A random mix operator for mutation selects a mutation variant 
        randomly.
	"""
	
	homepage = "<https://github.com/ageyerschulz/xegaPermGene>"
	cran = "xegaPermGene" 

	version("1.0.0.0", md5="c8028f9d6fc423eb7c1290d3f3712aee")

	depends_on("r-xegaselectgene", type=("build", "run"))
