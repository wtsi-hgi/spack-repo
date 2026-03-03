# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayeslm(RPackage):
	"""Efficient Sampling for Gaussian Linear Regression with Arbitrary
Priors

	Efficient sampling for Gaussian linear regression with arbitrary priors, Hahn, He and Lopes (2018) <arXiv:1806.05738>.
	"""
	
	homepage = "https://github.com/JingyuHe/bayeslm"
	cran = "bayeslm" 

	version("1.0.1", md5="3c994e5cea761bf5fd690b759e1beada")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
