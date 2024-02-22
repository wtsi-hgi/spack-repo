# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScout(RPackage):
	"""Implements the Scout Method for Covariance-Regularized
Regression

	Implements the Scout method for regression, described in "Covariance-regularized regression and classification for high-dimensional problems", by Witten and Tibshirani (2008),  Journal of the Royal Statistical Society, Series B 71(3): 615-636. 
	"""
	
	cran = "scout" 

	version("1.0.4", md5="d5ac064ec5c3c1beeaf5649319260e0d")

	depends_on("r-glasso", type=("build", "run"))
