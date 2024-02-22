# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFizzbuzzr(RPackage):
	"""Fizz Buzz Implementation

	An implementation of the Fizz Buzz algorithm, as defined e.g. in <https://en.wikipedia.org/wiki/Fizz_buzz>. 
    It provides the standard algorithm with 3 replaced by Fizz and 5 replaced by Buzz, with the option of specifying start 
    and end numbers, step size and the numbers being replaced by fizz and buzz, respectively. This package gives 
    interviewers the optional answer of "I use fizzbuzzR::fizzbuzz()" when interviewing rather than having to write an algorithm
    themselves.
	"""
	
	cran = "fizzbuzzR" 

	version("0.1.1", md5="875219ebc6d6729b629859a972673fc6")

	depends_on("r@3.1:", type=("build", "run"))
