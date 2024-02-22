# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIslasso(RPackage):
	"""The Induced Smoothed Lasso

	An implementation of the induced smoothing (IS) idea to lasso regularization models to allow estimation and inference on the model coefficients (currently hypothesis testing only). Linear, logistic, Poisson and gamma regressions with several link functions are implemented. The algorithm is described in the original paper; see <doi:10.1177/0962280219842890> and discussed in a tutorial <doi:10.13140/RG.2.2.16360.11521>.
	"""
	
	cran = "islasso" 

	version("1.5.2", md5="d10f3c07ed94751526d03b205b1ef374")

	depends_on("r-glmnet@4:", type=("build", "run"))
	depends_on("r-matrix@1.0.6:", type=("build", "run"))
	depends_on("r@4:", type=("build", "run"))
