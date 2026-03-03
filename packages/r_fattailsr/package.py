# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFattailsr(RPackage):
	"""Kiener Distributions and Fat Tails in Finance

	Kiener distributions K1, K2, K3, K4 and K7 to characterize
    distributions with left and right, symmetric or asymmetric fat tails in market
    finance, neuroscience and other disciplines. Two algorithms to estimate with
    a high accuracy distribution parameters, quantiles, value-at-risk and expected
    shortfall. Include power hyperbolas and power hyperbolic functions. 
	"""
	
	homepage = "https://www.inmodelia.com/fattailsr-en.html"
	cran = "FatTailsR" 

	version("1.8-5", md5="827470bc6e9c6a89d2ce9e6f14f38c6e")
	version("1.8-0", md5="66eb622321f0e917e32e2fe976788a14")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
	depends_on("r-timeseries", type=("build", "run"))
