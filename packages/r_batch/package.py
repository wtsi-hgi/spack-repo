# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBatch(RPackage):
	"""Batching Routines in Parallel and Passing Command-Line Arguments
to R

	Functions to allow you to easily pass command-line arguments into R, and functions to aid in submitting your R code in parallel on a cluster and joining the results afterward (e.g. multiple parameter values for simulations running in parallel, splitting up a permutation test in parallel, etc.). See `parseCommandArgs(...)' for the main example of how to use this package.
	"""
	
	homepage = "http://sites.google.com/site/thomashoffmannproject/"
	cran = "batch" 

	version("1.1-5", md5="20bf5e94e3c17263688df0394fd8a791")

	depends_on("r@2.14:", type=("build", "run"))
