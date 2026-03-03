# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBearishtrader(RPackage):
	"""Trading Strategies for Bearish Outlook

	Stock, Options and Futures Trading Strategies for Traders and Investors with Bearish Outlook. The indicators, strategies, calculations, functions and all other discussions are for academic, research, and educational purposes only and should not be construed as investment advice and come with absolutely no Liability.
    Guy Cohen (“The Bible of Options Strategies (2nd ed.)”, 2015, ISBN: 9780133964028).
    Juan A. Serur, Juan A. Serur (“151 Trading Strategies”, 2018, ISBN: 9783030027919).
    Chartered Financial Analyst Institute ("Chartered Financial Analyst Program Curriculum 2020 Level I Volumes 1-6. (Vol. 5, pp. 385-453)", 2019, ISBN: 9781119593577).
    John C. Hull (“Options, Futures, and Other Derivatives (11th ed.)”, 2022, ISBN: 9780136939979).
	"""
	
	cran = "bearishTrader" 

	version("1.0.2", md5="f72b83830a0bff2324c7f232a01d7f74")

