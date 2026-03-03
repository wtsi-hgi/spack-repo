# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDecorators(RPackage):
	"""Extend the Behaviour of a Function without Explicitly Modifying
it

	A decorator is a function that receives a function, extends
    its behaviour, and returned the altered function. Any caller that uses
    the decorated function uses the same interface as it were the
    original, undecorated function. Decorators serve two primary uses: (1)
    Enhancing the response of a function as it sends data to a second
    component; (2) Supporting multiple optional behaviours. An example of
    the first use is a timer decorator that runs a function, outputs its
    execution time on the console, and returns the original function's
    result. An example of the second use is input type validation
    decorator that during running time tests whether the caller has passed
    input arguments of a particular class.  Decorators can reduce
    execution time, say by memoization, or reduce bugs by adding defensive
    programming routines.
	"""
	
	homepage = "https://tidylab.github.io/decorators/"
	cran = "decorators" 

	version("0.3.0", md5="1132f781c957f56ea10f3a4b66fe7a87")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
