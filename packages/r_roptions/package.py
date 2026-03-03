# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRoptions(RPackage):
	"""Option Strategies and Valuation

	Collection of tools to develop options strategies, value option contracts using the Black-Scholes-Merten option pricing model and calculate the option Greeks. Hull, John C. "Options, Futures, and Other Derivatives" (1997, ISBN:0-13-601589-1). Fischer Black, Myron Scholes (1973) "The Pricing of Options and Corporate Liabilities" <doi:10.1086/260062>. 
	"""
	
	cran = "roptions" 

	version("1.0.3", md5="2b45ad145ec114c8c28ee54d7763f4a7")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
