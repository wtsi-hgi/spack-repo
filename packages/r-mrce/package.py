# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMrce(RPackage):
	"""Multivariate Regression with Covariance Estimation

	Compute and select tuning parameters for the MRCE estimator proposed by Rothman, Levina, and Zhu (2010) <doi:10.1198/jcgs.2010.09188>.  This estimator fits the multiple output linear regression model with a sparse estimator of the error precision matrix and a sparse estimator of the regression coefficient matrix.
	"""
	
	cran = "MRCE" 

	version("2.4", md5="d1460952daccfefaa1944887ed1c238e")

	depends_on("r@2.10.1:", type=("build", "run"))
	depends_on("r-glasso", type=("build", "run"))
