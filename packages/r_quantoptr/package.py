# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQuantoptr(RPackage):
	"""Algorithms for Quantile- And Mean-Optimal Treatment Regimes

	Estimation methods for optimal treatment regimes under three different criteria, namely marginal quantile, marginal mean, and mean absolute difference. For the first two criteria, both one-stage and two-stage estimation method are implemented. A doubly robust estimator for estimating the quantile-optimal treatment regime is also included. 
	"""
	
	cran = "quantoptr" 

	version("0.1.3", md5="3eb518c0f7caefb8975f8921b4bed1b9")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rgenoud@5.7:", type=("build", "run"))
	depends_on("r-quantreg@5.18:", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
