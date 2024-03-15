# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCryptoquotes(RPackage):
	"""A Streamlined Access to Cryptocurrency OHLC-V Market Data and
Sentiment Indicators

	
  This high-level API client offers a streamlined access to public cryptocurrency market data and sentiment indicators. It features OHLC-V (Open, High, Low, Close, Volume) that comes
  with granularity ranging from seconds to months and essential sentiment indicators to develop and backtest trading strategies, or conduct detailed market analysis. By interacting directly with
  the major cryptocurrency exchanges this package ensures a reliable, and stable, flow of market information, eliminating the need for complex, low-level API interactions or webcrawlers.
	"""
	
	homepage = "https://serkor1.github.io/cryptoQuotes/"
	cran = "cryptoQuotes" 

	version("1.3.0", md5="80df5f901e380db33eebb13e499fe858")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-cli@3.6.2:", type=("build", "run"))
	depends_on("r-conflicted@1.2:", type=("build", "run"))
	depends_on("r-curl@5.2:", type=("build", "run"))
	depends_on("r-jsonlite@1.8.8:", type=("build", "run"))
	depends_on("r-lifecycle@1.0.4:", type=("build", "run"))
	depends_on("r-paletteer@1.6:", type=("build", "run"))
	depends_on("r-plotly@4.10.4:", type=("build", "run"))
	depends_on("r-rlang@1.1.3:", type=("build", "run"))
	depends_on("r-ttr@0.24.4:", type=("build", "run"))
	depends_on("r-xts@0.13.2:", type=("build", "run"))
	depends_on("r-zoo@1.8.12:", type=("build", "run"))
