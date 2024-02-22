# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCryptoquotes(RPackage):
	"""A Streamlined Access to OHLC-v Market Data and Sentiment
Indicators

	This high-level API client offers a streamlined access to comprehensive cryptocurrency market data from major exchanges. 
  It features robust OHLC-V (Open, High, Low, Close, Volume) candle data with flexible granularity, ranging from seconds to months, and includes insightful sentiment indicators. 
  By aggregating data directly from leading exchanges, this package ensures a reliable and stable flow of market information, eliminating the need for complex, low-level API interactions.
	"""
	
	homepage = "https://serkor1.github.io/cryptoQuotes/"
	cran = "cryptoQuotes" 

	version("1.2.1", md5="2fd282048d29a804d5642b61a6f75667")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-curl@5.1:", type=("build", "run"))
	depends_on("r-httr2", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-magrittr@2.0.3:", type=("build", "run"))
	depends_on("r-plotly@4.10.2:", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rlang@1.1.1:", type=("build", "run"))
	depends_on("r-ttr", type=("build", "run"))
	depends_on("r-xts@0.13.1:", type=("build", "run"))
	depends_on("r-zoo@1.8.12:", type=("build", "run"))
