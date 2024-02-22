# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFishmod(RPackage):
	"""Fits Poisson-Sum-of-Gammas GLMs, Tweedie GLMs, and Delta
Log-Normal Models

	Fits models to catch and effort data. Single-species models are 1) delta log-normal, 2) Tweedie, or 3) Poisson-gamma (G)LMs.
	"""
	
	cran = "fishMod" 

	version("0.29", md5="ac6dc16674f459850e7e19760e8beeee")

