# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAgtboost(RPackage):
	"""Adaptive and Automatic Gradient Boosting Computations

	Fast and automatic gradient tree boosting designed
    to avoid manual tuning and cross-validation by utilizing an information
    theoretic approach. This makes the algorithm adaptive to the dataset at
    hand; it is completely automatic, and with minimal worries of overfitting.
    Consequently, the speed-ups relative to state-of-the-art implementations
    can be in the thousands while mathematical and technical knowledge required
    on the user are minimized.
	"""
	
	cran = "agtboost" 

	version("0.9.3", md5="cee2d026ed67c696cf9cca4169b725ba")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
