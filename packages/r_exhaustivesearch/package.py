# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExhaustivesearch(RPackage):
	"""A Fast and Scalable Exhaustive Feature Selection Framework

	The goal of this package is to provide an easy to use, fast and
    scalable exhaustive search framework. Exhaustive feature selections 
    typically require a very large number of models to be fitted and evaluated. 
    Execution speed and memory management are crucial factors here. This package 
    provides solutions for both. Execution speed is optimized by using a 
    multi-threaded C++ backend, and memory issues are solved by by only storing 
    the best results during execution and thus keeping memory usage constant.
	"""
	
	homepage = "https://github.com/RudolfJagdhuber/ExhaustiveSearch"
	cran = "ExhaustiveSearch" 

	version("1.0.1", md5="ff33cf11bc9bcbf4c1ecbc4700e91064")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
