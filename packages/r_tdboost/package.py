# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTdboost(RPackage):
	"""A Boosted Tweedie Compound Poisson Model

	An implementation of a boosted Tweedie compound Poisson model proposed by Yang, Y., Qian, W. and Zou, H. (2018) <doi:10.1080/07350015.2016.1200981>. It is capable of fitting a flexible nonlinear Tweedie compound Poisson model (or a gamma model) and capturing high-order interactions among predictors. This package is based on the 'gbm' package originally developed by Greg Ridgeway.
	"""
	
	cran = "TDboost" 

	version("1.5", md5="af78c668950b797017fda80c56b78ba7")

	depends_on("r@2.12:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
