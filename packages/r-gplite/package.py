# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGplite(RPackage):
	"""General Purpose Gaussian Process Modelling

	
  Implements the most common Gaussian process (GP) models using Laplace and
  expectation propagation (EP) approximations, maximum marginal likelihood
  (or posterior) inference for the hyperparameters, and sparse approximations
  for larger datasets.
	"""
	
	cran = "gplite" 

	version("0.13.0", md5="f13531c115adfc82333dfd8daec8e328")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
