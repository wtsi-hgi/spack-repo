# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKtweedie(RPackage):
	"""'Tweedie' Compound Poisson Model in the Reproducing Kernel
Hilbert Space

	Kernel-based 'Tweedie' compound Poisson gamma model using high-dimensional predictors for the analyses of zero-inflated response variables. The package features built-in estimation, prediction and cross-validation tools and supports choice of different kernel functions. For more details, please see Yi Lian, Archer Yi Yang, Boxiang Wang, Peng Shi & Robert William Platt (2023) <doi:10.1080/00401706.2022.2156615>.
	"""
	
	cran = "ktweedie" 

	version("1.0.3", md5="745b71574a0370ce5526d5054ad18d15")

	depends_on("r@3.5:", type=("build", "run"))
