# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRobustreg(RPackage):
	"""Robust Regression Functions

	Linear regression functions using Huber and bisquare psi functions. Optimal weights are calculated using IRLS algorithm.
	"""
	
	cran = "robustreg" 

	version("0.1-11", md5="3cbc3aa371183317c00226ab5075e5f5")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-matrix@1.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
