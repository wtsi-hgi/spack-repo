# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXegaselectgene(RPackage):
	"""Selection of Genes and Gene Representation Independent Functions

	This collection of gene representation-independent 
             mechanisms for evolutionary and genetic algorithms contains
             four groups of functions:
             First, functions for selecting a gene 
             in a population of genes according to its fitness value
             and for adaptive scaling of the fitness values as well as for 
             performance optimization and measurement offer several 
             variants for implementing the survival of the fittest.
             Second, evaluation functions for 
             deterministic functions avoid recomputation.
             Evaluation of stochastic functions incrementally improve 
             the estimation of the mean and variance of fitness values 
             at almost no additional cost. Evaluation functions
             for gene repair handle error-correcting decoders.
             Third, timing and counting functions for profiling the
             algorithm pipeline are provided to assess bottlenecks in 
             the algorithms.
             Fourth, a small collection of problem environments
             for function optimization, combinatorial optimization, and
             grammar-based genetic programming and grammatical evolution
             is provided for tutorial examples.
             The methods in the package are described by the following
             references:
             Baker, James E. (1987, ISBN:978-08058-0158-8), 
             De Jong, Kenneth A. (1975) 
             <https://deepblue.lib.umich.edu/handle/2027.42/4507>,
             Geyer-Schulz, Andreas (1997, ISBN:978-3-7908-0830-X),
             Grefenstette, John J. (1987, ISBN:978-08058-0158-8),
             Grefenstette, John J. and Baker, James E. 
             (1989, ISBN:1-55860-066-3),
             Holland, John (1975, ISBN:0-472-08460-7),
             Lau, H. T. (1986) <doi:10.1007/978-3-642-61649-5>,
             Price, Kenneth V., Storn, Rainer M. and Lampinen, Jouni A. (2005) 
             <doi:10.1007/3-540-31306-0>,  
             Reynolds, J. C. (1993) <doi:10.1007/BF01019459>,
             Schaffer, J. David (1989, ISBN:1-55860-066-3),
             Wenstop, Fred (1980) <doi:10.1016/0165-0114(80)90031-7>,
             Whitley, Darrell (1989, ISBN:1-55860-066-3),
             Wickham, Hadley (2019, ISBN:978-815384571).
	"""
	
	homepage = "<https://github.com/ageyerschulz/xegaSelectGene>"
	cran = "xegaSelectGene" 

	version("1.0.0.0", md5="a18ba8d7f2674e4a8a0d0e28b9d10755")

