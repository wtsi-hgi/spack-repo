# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBullishtrader(RPackage):
	"""Bullish Trading Strategies Through Graphs

	Stock, Options and Futures Trading Strategies for Traders and Investors with Bullish Outlook are represented here through their Graphs. The graphic indicators, strategies, calculations, functions and all the discussions are for academic, research, and educational purposes only and should not be construed as investment advice and come with absolutely no Liability.
    Guy Cohen (“The Bible of Options Strategies (2nd ed.)”, 2015, ISBN: 9780133964028).
    Zura Kakushadze, Juan A. Serur (“151 Trading Strategies”, 2018, ISBN: 9783030027919).
    John C. Hull (“Options, Futures, and Other Derivatives (11th ed.)”, 2022, ISBN: 9780136939979).
	"""
	
	cran = "bullishTrader" 

	version("1.0.1", md5="7cbfe282e0abba38ff28a889a6dc6a70")

