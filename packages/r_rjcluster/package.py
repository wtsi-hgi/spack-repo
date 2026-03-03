# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRjcluster(RPackage):
	"""A Fast Clustering Algorithm for High Dimensional Data Based on
the Gram Matrix Decomposition

	Clustering algorithm for high dimensional data. Assuming that P feature measurements on N objects are arranged in an N×P matrix X, this package provides clustering based on the left Gram matrix XX^T. To simulate test data, type "help('simulate_HD_data')" and to learn how to use the clustering algorithm, type "help('RJclust')". To cite this package, type 'citation("RJcluster")'. 
	"""
	
	cran = "RJcluster" 

	version("3.2.4", md5="c45a59bb73bc50e6bd8682968237a631")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-infotheo", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-profvis", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
