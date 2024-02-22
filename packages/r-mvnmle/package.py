# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMvnmle(RPackage):
	"""ML Estimation for Multivariate Normal Data with Missing Values

	Finds the Maximum Likelihood (ML) Estimate of the mean vector
        and variance-covariance matrix for multivariate normal data
        with missing values.
	"""
	
	homepage = "https://github.com/indenkun/mvnmle"
	cran = "mvnmle" 

	version("0.1-11.2", md5="85dca87d9b73e74f09b9b042c0e4817f")

