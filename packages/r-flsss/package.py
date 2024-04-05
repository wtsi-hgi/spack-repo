# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlsss(RPackage):
	"""Mining Rigs for Problems in the Subset Sum Family

	Specialized solvers for combinatorial optimization problems in the Subset Sum family. The solvers differ from the mainstream in the options of (i) restricting subset size, (ii) bounding subset elements, (iii) mining real-value multisets with predefined subset sum errors, (iv) finding one or more subsets in limited time. A novel algorithm for mining the one-dimensional Subset Sum induced algorithms for the multi-Subset Sum and the multidimensional Subset Sum. The multi-threaded framework for the latter offers exact algorithms to the multidimensional Knapsack and the Generalized Assignment problems. Historical updates include (a) renewed implementation of the multi-Subset Sum, multidimensional Knapsack and Generalized Assignment solvers; (b) availability of bounding solution space in the multidimensional Subset Sum; (c) fundamental data structure and architectural changes for enhanced cache locality and better chance of SIMD vectorization; (d) option of mapping floating-point instance to compressed 64-bit integer instance with user-controlled precision loss, which could yield substantial speedup due to the dimension reduction and efficient compressed integer arithmetic via bit-manipulations; (e) distributed computing infrastructure for multidimensional subset sum; (f) arbitrary-precision zero-margin-of-error multidimensional Subset Sum accelerated by a simplified Bloom filter. The package contains a copy of xxHash from <https://github.com/Cyan4973/xxHash>. Package vignette (<arXiv:1612.04484v3>) detailed a few historical updates. Functions prefixed with 'aux' (auxiliary) are independent implementations of published algorithms for solving optimization problems less relevant to Subset Sum.
	"""
	
	cran = "FLSSS" 

	version("9.1.3", md5="586fbc366f159be23c310cf70e06f88a")
	version("9.1.1", md5="6774232dee3c5fe09cdd9cd54968b556")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
