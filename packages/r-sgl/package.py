# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSgl(RPackage):
	"""Fit a GLM (or Cox Model) with a Combination of Lasso and Group
Lasso Regularization

	Fit a regularized generalized linear model via penalized
        maximum likelihood.  The model is fit for a path of values of
        the penalty parameter. Fits linear, logistic and Cox models.
	"""
	
	cran = "SGL" 

	version("1.3", md5="9dc5f0ca54db3a3f7dd520730b62545c")

