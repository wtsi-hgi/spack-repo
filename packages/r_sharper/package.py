# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSharper(RPackage):
	"""Statistical Significance of the Sharpe Ratio

	A collection of tools for analyzing significance of assets,
    funds, and trading strategies, based on the Sharpe ratio and overfit 
    of the same. Provides density, distribution, quantile and random generation 
    of the Sharpe ratio distribution based on normal returns, as well
    as the optimal Sharpe ratio over multiple assets. Computes confidence intervals
    on the Sharpe and provides a test of equality of Sharpe ratios based on 
    the Delta method. The statistical foundations of the Sharpe can be found in
    the author's Short Sharpe Course  <doi:10.2139/ssrn.3036276>.
	"""
	
	homepage = "https://github.com/shabbychef/SharpeR"
	cran = "SharpeR" 

	version("1.3.0", md5="1f045f6975cb81bcccdff34e1d455ce5")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
