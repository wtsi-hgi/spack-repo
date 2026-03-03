# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGmkmcharlie(RPackage):
	"""Unsupervised Gaussian Mixture and Minkowski and Spherical
K-Means with Constraints

	High performance trainers for parameterizing and clustering weighted data. The Gaussian mixture (GM) module includes the conventional EM (expectation maximization) trainer, the component-wise EM trainer, the minimum-message-length EM trainer by Figueiredo and Jain (2002) <doi:10.1109/34.990138>. These trainers accept additional constraints on mixture weights, covariance eigen ratios and on which mixture components are subject to update. The K-means (KM) module offers clustering with the options of (i) deterministic and stochastic K-means++ initializations, (ii) upper bounds on cluster weights (sizes), (iii) Minkowski distances, (iv) cosine dissimilarity, (v) dense and sparse representation of data input. The package improved the typical implementations of GM and KM algorithms in various aspects. It is carefully crafted in multithreaded C++ for modeling large data for industry use.
	"""
	
	cran = "GMKMcharlie" 

	version("1.1.5", md5="5193ea87e9250e8b7dba09c1d80d99e0")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
