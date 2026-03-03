# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMniw(RPackage):
	"""The Matrix-Normal Inverse-Wishart Distribution

	Density evaluation and random number generation for the Matrix-Normal Inverse-Wishart (MNIW) distribution, as well as the the Matrix-Normal, Matrix-T, Wishart, and Inverse-Wishart distributions.  Core calculations are implemented in a portable (header-only) C++ library, with matrix manipulations using the 'Eigen' library for linear algebra.  Also provided is a Gibbs sampler for Bayesian inference on a random-effects model with multivariate normal observations.
	"""
	
	homepage = "https://github.com/mlysy/mniw/"
	cran = "mniw" 

	version("1.0.1", md5="68b02a5fca9afcf5dceeb2c9f2c10e2e")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
