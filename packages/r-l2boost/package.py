# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RL2boost(RPackage):
	"""Exploring Friedman's Boosting Algorithm for Regularized Linear
Regression

	Efficient implementation of Friedman's boosting algorithm with
    l2-loss function and coordinate direction (design matrix columns) basis
    functions.
	"""
	
	cran = "l2boost" 

	version("1.0.3", md5="7bbfb950dfe4e88eca88e63bfb8791da")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
