# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRamchoice(RPackage):
	"""Revealed Preference and Attention Analysis in Random Limited
Attention Models

	It is widely documented in psychology, economics and other disciplines that socio-economic agent may not pay full attention to all available alternatives, rendering standard revealed preference theory invalid. This package implements the estimation and inference procedures of Cattaneo, Ma, Masatlioglu and Suleymanov (2020) <arXiv:1712.03448> and Cattaneo, Cheung, Ma, and Masatlioglu (2022) <arXiv:2110.10650>, which utilizes standard choice data to partially identify and estimate a decision maker's preference and attention. For inference, several simulation-based critical values are provided. 
	"""
	
	cran = "ramchoice" 

	version("2.2", md5="600a5522f6a5720c7a10835e389f9f6d")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
