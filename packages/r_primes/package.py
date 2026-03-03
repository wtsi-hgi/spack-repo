# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrimes(RPackage):
	"""Fast Functions for Prime Numbers

	Fast functions for dealing with prime numbers, such as testing
    whether a number is prime and generating a sequence prime numbers.
    Additional functions include finding prime factors and Ruth-Aaron pairs,
    finding next and previous prime numbers in the series, finding or estimating
    the nth prime, estimating the number of primes less than or equal to an
    arbitrary number, computing primorials, prime k-tuples (e.g., twin primes),
    finding the greatest common divisor and smallest (least) common multiple,
    testing whether two numbers are coprime, and computing Euler's totient
    function. Most functions are vectorized for speed and convenience.
	"""
	
	homepage = "https://github.com/ironholds/primes"
	cran = "primes" 

	version("1.6.0", md5="198d39170120e639f1bf022cd7466f0f")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
