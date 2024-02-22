# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRrat(RPackage):
	"""Robust Regression with Asymmetric Heavy-Tail Noise Distributions

	Implementation of Robust Regression tailored to deal with Asymmetric noise Distribution, which was originally proposed by Takeuchi & Bengio & Kanamori (2002) <doi:10.1162/08997660260293300>. In addition, this implementation is extended as introducing potential feature regularization by LASSO etc.
	"""
	
	cran = "rrat" 

	version("1.0.0", md5="48222fe857df48af9f8135390e7e79cd")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
