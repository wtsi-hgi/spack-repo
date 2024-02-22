# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStrategy(RPackage):
	"""Generic Framework to Analyze Trading Strategies

	Users can build and test customized quantitative trading strategies. Some quantitative trading strategies are already implemented, e.g. various moving-average filters with trend following approaches.
    The implemented class called "Strategy" allows users to access several methods to analyze performance figures, plots and backtest the strategies.
    Furthermore, custom strategies can be added, a generic template is available. The custom strategies require a certain input and output so they can be called from the Strategy-constructor.
	"""
	
	cran = "Strategy" 

	version("1.0.1", md5="2acd1eeb2ef6aac63bd0442d835c0ac6")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
