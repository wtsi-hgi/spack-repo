# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXega(RPackage):
	"""Extended Evolutionary and Genetic Algorithms

	
        Implementation of a scalable, highly configurable, and 
        e(x)tended architecture for (e)volutionary and (g)enetic (a)lgorithms.
        Multiple representations (binary, real-coded, permutation, and 
        derivation-tree), a rich collection of genetic operators, 
        as well as an extended processing pipeline are provided 
        for genetic algorithms (Goldberg, D. E. (1989, ISBN:0-201-15767-5)),
        differential evolution (Price, Kenneth V., Storn, Rainer M. and Lampinen, Jouni A. (2005)
        <doi:10.1007/3-540-31306-0>), simulated annealing (Aarts, E., and Korst, J.
        (1989, ISBN:0-471-92146-7)), grammar-based genetic programming 
        (Geyer-Schulz (1997, ISBN:978-3-7908-0830-X)), and grammatical evolution 
        (Ryan, C., O'Neill, M., and Collins, J. J. (2018) <doi:10.1007/978-3-319-78717-6>).
        All algorithms reuse basic adaptive mechanisms for performance optimization.
        Sequential or parallel execution (on multi-core machines, 
        local clusters, and high performance computing environments) 
        is available for all algorithms. See 
        <https://github.com/ageyerschulz/xega/tree/main/examples/executionModel>.
	"""
	
	homepage = "<https://github.com/ageyerschulz/xega>"
	cran = "xega" 

	version("0.9.0.0", md5="94e71d054cda915d5ded26841b181bca")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-parallelly", type=("build", "run"))
	depends_on("r-xegaselectgene", type=("build", "run"))
	depends_on("r-xegabnf", type=("build", "run"))
	depends_on("r-xegaderivationtrees", type=("build", "run"))
	depends_on("r-xegagagene", type=("build", "run"))
	depends_on("r-xegagpgene", type=("build", "run"))
	depends_on("r-xegagegene", type=("build", "run"))
	depends_on("r-xegadfgene", type=("build", "run"))
	depends_on("r-xegapermgene", type=("build", "run"))
	depends_on("r-xegapopulation", type=("build", "run"))
