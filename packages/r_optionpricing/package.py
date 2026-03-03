# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROptionpricing(RPackage):
	"""Option Pricing with Efficient Simulation Algorithms

	Efficient Monte Carlo Algorithms for the price and the sensitivities of Asian and European Options under Geometric Brownian Motion.
	"""
	
	cran = "OptionPricing" 

	version("0.1.2", md5="d8ff4006d1af03ee538a09b4f87e72c6")

