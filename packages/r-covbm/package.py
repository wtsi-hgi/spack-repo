# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCovbm(RPackage):
	"""Brownian Motion Processes for 'nlme'-Models

	Allows Brownian motion, fractional Brownian motion,
    and integrated Ornstein-Uhlenbeck process components to
    be added to linear and non-linear mixed effects models
    using the structures and methods of the 'nlme' package.
	"""
	
	cran = "covBM" 

	version("0.1.0", md5="68e6d415aa43b66ac0fc145029bdad50")

	depends_on("r-nlme@3:", type=("build", "run"))
