# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStdmod(RPackage):
	"""Standardized Moderation Effect and Its Confidence Interval

	Functions for computing a standardized moderation effect
             in moderated regression and forming its confidence interval
             by nonparametric bootstrapping as proposed in
             Cheung, Cheung, Lau, Hui, and Vong (2022)
             <doi:10.1037/hea0001188>. Also includes simple-to-use
             functions for computing conditional effects (unstandardized
             or standardized) and plotting moderation effects.
	"""
	
	homepage = "https://sfcheung.github.io/stdmod/"
	cran = "stdmod" 

	version("0.2.10", md5="f6fd0588a79516e6135672b21126660c")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
	depends_on("r-manymome", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
