# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSkm(RPackage):
	"""Selective k-Means

	Algorithms for solving selective k-means problem,
    which is defined as finding k rows in an m x n matrix such that 
    the sum of each column minimal is minimized. 
    In the scenario when m == n and each cell value in matrix is a 
    valid distance metric, this is equivalent to a k-means problem. 
    The selective k-means extends the k-means problem in the sense 
    that it is possible to have m != n, often the case m < n which 
    implies the search is limited within a small subset of rows. 
    Also, the selective k-means extends the k-means problem in the 
    sense that the instance in row set can be instance not seen in 
    the column set, e.g., select 2 from 3 internet service provider
    (row) for 5 houses (column) such that minimize the overall cost 
    (cell value) - overall cost is the sum of the column minimal of
    the selected 2 service provider.
	"""
	
	homepage = "http://github.com/gyang274/skm"
	cran = "skm" 

	version("0.1.5.4", md5="c92d0edaef31363af87b687dbe9d9e8f")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
