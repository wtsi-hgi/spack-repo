# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProxyc(RPackage):
	"""Computes Proximity in Large Sparse Matrices

	
    Computes proximity between rows or columns of large matrices efficiently in C++.
    Functions are optimised for large sparse matrices using the Armadillo and Intel TBB libraries.
    Among several built-in similarity/distance measures, computation of correlation,
    cosine similarity and Euclidean distance is particularly fast.
	"""
	
	homepage = "https://github.com/koheiw/proxyC"
	cran = "proxyC" 

	version("0.3.4", md5="e57fe4d1fd003337b06845fe6c8cd591")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-matrix@1.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.7.600.1:", type=("build", "run"))
