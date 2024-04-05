# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQrmdata(RPackage):
	"""Data Sets for Quantitative Risk Management Practice

	Various data sets (stocks, stock indices, constituent data, FX,
 zero-coupon bond yield curves, volatility, commodities) for Quantitative
 Risk Management practice.
	"""
	
	cran = "qrmdata" 

	version("2024-03-04-2", md5="d7a09c8587fde3554c3b68c79d53316f")
	version("2022-05-31-1", md5="f9cfd74dc6f33d2125064eb65d6dbe30")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
