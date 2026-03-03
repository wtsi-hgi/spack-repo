# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNpregderiv(RPackage):
	"""Nonparametric Estimation of the Derivatives of a Regression
Function

	Estimating the first and second derivatives of a regression function by the method of Wang and Lin (2015) <http://www.jmlr.org/papers/v16/wang15b.html>.
	"""
	
	cran = "npregderiv" 

	version("1.0", md5="c9d5ff0185b1c17ba20fb47bd03223dd")

	depends_on("r@3.1:", type=("build", "run"))
