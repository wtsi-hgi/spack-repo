# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNumbers(RPackage):
	"""Number-Theoretic Functions

	
    Provides number-theoretic functions for factorization, prime 
    numbers, twin primes, primitive roots, modular logarithm and
    inverses, extended GCD, Farey series and continued fractions.
    Includes Legendre and Jacobi symbols, some divisor functions,
    Euler's Phi function, etc.
	"""
	
	cran = "numbers" 

	version("0.8-5", md5="3f9d482326ca6c5360df4f49c0849c2f")

	depends_on("r@4.1:", type=("build", "run"))
