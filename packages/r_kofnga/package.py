# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKofnga(RPackage):
	"""A Genetic Algorithm for Fixed-Size Subset Selection

	Provides a function that uses a genetic algorithm to search for a subset
 of size k from the integers 1:n, such that a user-supplied objective function 
 is minimized at that subset.  The selection step is done by tournament selection 
 based on ranks, and elitism may be used to retain a portion of the best solutions 
 from one generation to the next. Population objective function values may 
 optionally be evaluated in parallel.
	"""
	
	cran = "kofnGA" 

	version("1.3", md5="35d1e5699a4eb2de47d9ebe7560cdfbd")

	depends_on("r-bigmemory", type=("build", "run"))
