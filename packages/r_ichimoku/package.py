# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIchimoku(RPackage):
	"""Visualization and Tools for Ichimoku Kinko Hyo Strategies

	An implementation of 'Ichimoku Kinko Hyo', also commonly known as
    'cloud charts'. Static and interactive visualizations with tools for
    creating, backtesting and development of quantitative 'ichimoku' strategies.
    As described in Sasaki (1996, ISBN:4925152009), the technique is a refinement
    on candlestick charting, originating from Japan and now in widespread use in
    technical analysis worldwide. Translating as 'one-glance equilibrium chart',
    it allows the price action and market structure of financial securities to
    be determined 'at-a-glance'. Incorporates an interface with the OANDA
    fxTrade API <https://developer.oanda.com/> for retrieving historical and
    live streaming price data for major currencies, metals, commodities,
    government bonds and stock indices.
	"""
	
	homepage = "https://shikokuchuo.net/ichimoku/"
	cran = "ichimoku" 

	version("1.5.0", md5="e34ee2af7a52bb7ea33e407d2186aec1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-mirai@0.12:", type=("build", "run"))
	depends_on("r-nanonext@0.12:", type=("build", "run"))
	depends_on("r-rcppsimdjson", type=("build", "run"))
	depends_on("r-secretbase", type=("build", "run"))
	depends_on("r-shiny@1.4:", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
