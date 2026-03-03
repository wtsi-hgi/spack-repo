# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVerylargeintegers(RPackage):
	"""Store and Operate with Arbitrarily Large Integers

	Multi-precision library that allows to store and operate with arbitrarily big integers without
    loss of precision. It includes a large list of tools to work with them, like:
      - Arithmetic and logic operators
      - Modular-arithmetic operators
      - Computer Number Theory utilities
      - Probabilistic primality tests
      - Factorization algorithms
      - Random generators of diferent types of integers.
	"""
	
	cran = "VeryLargeIntegers" 

	version("0.2.1", md5="44b762882d0c43a4d761c7389857b060")

	depends_on("r-rcpp", type=("build", "run"))
