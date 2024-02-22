# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCombiter(RPackage):
	"""Combinatorics Iterators

	Provides iterators for combinations, permutations, subsets, and
    Cartesian product, which allow one to go through all elements without creating a
    huge set of all possible values.
	"""
	
	homepage = "https://github.com/kota7/combiter"
	cran = "combiter" 

	version("1.0.3", md5="a25aab295bc9a2f0ad62f90685ca2ba8")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-itertools", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
