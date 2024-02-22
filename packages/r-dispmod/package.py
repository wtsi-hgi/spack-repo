# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDispmod(RPackage):
	"""Modelling Dispersion in GLM

	Functions for estimating Gaussian dispersion regression models (Aitkin, 1987 <doi:10.2307/2347792>), overdispersed binomial logit models (Williams, 1987 <doi:10.2307/2347977>), and overdispersed Poisson log-linear models (Breslow, 1984 <doi:10.2307/2347661>), using a quasi-likelihood approach.
	"""
	
	cran = "dispmod" 

	version("1.2", md5="39286bf3fa0a14d8aa1f28bfc6012f02")

	depends_on("r@3:", type=("build", "run"))
