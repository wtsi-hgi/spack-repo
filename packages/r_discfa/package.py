# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiscfa(RPackage):
	"""Discrete Factor Analysis

	Discrete factor analysis for dependent Poisson and negative binomial models with truncation, zero inflation, and zero inflated truncation.
	"""
	
	cran = "discFA" 

	version("1.0.1", md5="f21adb5c8f1f61523705ccb69d843c93")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
