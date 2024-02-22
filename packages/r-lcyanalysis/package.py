# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLcyanalysis(RPackage):
	"""Stock Data Analysis Functions

	Analysis of stock data ups and downs trend, the stock technical analysis indicators function have trend line, reversal pattern and market trend.
	"""
	
	cran = "lcyanalysis" 

	version("1.0.4", md5="777c907b85916616828ca09f0773e49d")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-quantmod", type=("build", "run"))
	depends_on("r-ttr", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
