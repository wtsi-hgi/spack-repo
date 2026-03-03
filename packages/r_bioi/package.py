# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBioi(RPackage):
	"""Biological Image Analysis

	Single linkage clustering and connected component analyses are often performed on biological images. 'Bioi' provides a set of functions for performing these tasks. This functionality is implemented in several key functions that can extend to from 1 to many dimensions. The single linkage clustering method implemented here can be used on n-dimensional data sets, while connected component analyses are limited to 3 or fewer dimensions.
	"""
	
	cran = "Bioi" 

	version("0.2.10", md5="0a3bf55ff3f8c2bf51d1d505d5914d91")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-assertthat@0.2:", type=("build", "run"))
	depends_on("r-dplyr@0.7.4:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
