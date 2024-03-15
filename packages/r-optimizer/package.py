# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROptimizer(RPackage):
	"""Unified Framework for Numerical Optimizers

	Provides a unified object-oriented framework for numerical 
    optimizers in R. Allows for both minimization and maximization with any 
    optimizer, optimization over more than one function argument, measuring of 
    computation time, setting a time limit for long optimization tasks.
	"""
	
	homepage = "https://loelschlaeger.de/optimizeR/"
	cran = "optimizeR" 

	version("1.0.5", md5="4b8360a86a20c1a13945cedc13086937")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-lbfgsb3c", type=("build", "run"))
	depends_on("r-oeli@0.4.1:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-testfunctions", type=("build", "run"))
	depends_on("r-ucminf", type=("build", "run"))
