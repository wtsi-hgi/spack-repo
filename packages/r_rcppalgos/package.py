# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcppalgos(RPackage):
	"""High Performance Tools for Combinatorics and Computational
Mathematics

	Provides optimized functions and flexible combinatorial iterators
    implemented in C++ for solving problems in combinatorics and
    computational mathematics. Utilizes the RMatrix class from 'RcppParallel'
    for thread safety. There are combination/permutation functions with
    constraint parameters that allow for generation of all results of a vector
    meeting specific criteria (e.g. generating integer partitions/compositions
    or finding all combinations such that the sum is between two bounds).
    Capable of generating specific combinations/permutations (e.g. retrieve
    only the nth lexicographical result) which sets up nicely for
    parallelization as well as random sampling. Gmp support permits exploration
    where the total number of results is large (e.g. comboSample(10000, 500,
    n = 4)). Additionally, there are several high performance number theoretic
    functions that are useful for problems common in computational mathematics.
    Some of these functions make use of the fast integer division library
    'libdivide'. The primeSieve function is based on the segmented sieve of
    Eratosthenes implementation by Kim Walisch. It is also efficient for large
    numbers by using the cache friendly improvements originally developed by
    Tomás Oliveira. Finally, there is a prime counting function that implements
    Legendre's formula based on the work of Kim Walisch.
	"""
	
	homepage = "https://github.com/jwood000/RcppAlgos"
	cran = "RcppAlgos" 

	version("2.8.3", md5="fa5357670487c5e7e98c80cabd0318ce")

	depends_on("r-gmp", type=("build", "run"))
	depends_on("r-cpp11", type=("build", "run"))
	depends_on("gmp@4.2.3:", type=("build", "link", "run"))
