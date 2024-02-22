# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRpredictit(RPackage):
	"""Interface to the 'PredictIt' API

	Wrapper to retrieve market data, explore available markets, and plot historical price data from the 'PredictIt' public API (<https://www.predictit.org/api/marketdata/all/>).
    The package comes with a demo 'shiny' application for illustrating example use cases.
    License to use data made available via the API is for non-commercial use and 'PredictIt' is the sole source of such data.
	"""
	
	homepage = "https://github.com/danielkovtun/rpredictit"
	cran = "rpredictit" 

	version("0.1.0", md5="13581a49703e8f5ceaacac18f3a24b1f")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-dygraphs", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-quantmod", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
