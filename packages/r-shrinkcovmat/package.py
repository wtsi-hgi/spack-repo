# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShrinkcovmat(RPackage):
	"""Shrinkage Covariance Matrix Estimators

	Provides nonparametric Steinian shrinkage estimators of the covariance matrix that are suitable in high dimensional settings, that is when the number of variables is larger than the sample size.
	"""
	
	homepage = "http://github.com/AnestisTouloumis/ShrinkCovMat"
	cran = "ShrinkCovMat" 

	version("1.4.0", md5="8ac1dc0384866b6b65d05e11c119f6d6")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
