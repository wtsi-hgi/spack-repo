# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQuantbondcurves(RPackage):
	"""Calculates Bond Values and Interest Rate Curves for Finance

	Values different types of assets and calibrates discount curves 
    for quantitative financial analysis. It covers fixed coupon assets, 
    floating note assets, interest and cross currency swaps with different 
    payment frequencies. Enables the calibration of spot, instantaneous forward 
    and basis curves, making it a powerful tool for accurate and flexible bond 
    valuation and curve generation. The valuation and calibration techniques 
    presented here are consistent with industry standards and incorporates 
    author's own calculations. Tuckman, B., Serrat, A. (2022, ISBN: 978-1-119-83555-4).
	"""
	
	cran = "QuantBondCurves" 

	version("0.2.0", md5="f229d5001d7f6de57346ec4cb801c966")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-quantdates", type=("build", "run"))
	depends_on("r-rsolnp", type=("build", "run"))
