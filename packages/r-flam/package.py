# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlam(RPackage):
	"""Fits Piecewise Constant Models with Data-Adaptive Knots

	Implements the fused lasso additive model as proposed in Petersen, A., Witten, D., and Simon, N. (2016). Fused Lasso Additive Model. Journal of Computational and Graphical Statistics, 25(4): 1005-1025.
	"""
	
	cran = "flam" 

	version("3.2", md5="d20d2ecdb01d18b13886e7a148a13e62")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
