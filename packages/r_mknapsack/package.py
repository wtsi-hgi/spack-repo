# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMknapsack(RPackage):
	"""Multiple Knapsack Problem Solver

	Package solves multiple knapsack optimisation problem. 
    Given a set of items, each with volume and value, 
    it will allocate them to knapsacks of a given size in a way that
    value of top N knapsacks is as large as possible.
	"""
	
	homepage = "https://github.com/madedotcom/mknapsack"
	cran = "mknapsack" 

	version("0.1.0", md5="2862801dafef5c042feee35797ef02f8")

	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-lpsolve", type=("build", "run"))
