# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTriosgl(RPackage):
	"""Trio Model with a Combination of Lasso and Group Lasso
Regularization

	Fit a trio model via penalized maximum likelihood. The model is fit for a path of values of the penalty parameter. This package is based on Noah Simon, et al. (2011) <doi:10.1080/10618600.2012.681250>.
	"""
	
	cran = "TrioSGL" 

	version("1.1.0", md5="cd27826ab109eb6d4503aed577544860")

