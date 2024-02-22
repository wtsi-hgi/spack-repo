# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIncgraph(RPackage):
	"""Incremental Graphlet Counting for Network Optimisation

	An efficient and incremental approach for calculating 
    the differences in orbit counts when performing single edge modifications 
    in a network. Calculating the differences in orbit counts is much more efficient than
    recalculating all orbit counts from scratch for each time point.
	"""
	
	homepage = "http://www.github.com/rcannood/incgraph"
	cran = "incgraph" 

	version("1.0.1", md5="35275ddb84bec990bd7bb2e12afaa30c")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-orca", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
