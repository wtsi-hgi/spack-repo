# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPingers(RPackage):
	"""Identify, Ping, and Log Internet Provider Connection Data

	To assist you with troubleshooting internet connection issues and
    assist in isolating packet loss on your network. It does this by allowing you to 
    retrieve the top trace route destinations your internet provider uses, and recursively 
    ping each server in series while capturing the results and writing them to a log file. 
    Each iteration it queries the destinations again, before shuffling the sequence of 
    destinations to ensure the analysis is unbiased and consistent across each trace route.
	"""
	
	homepage = "https://github.com/JesseVent/pingers"
	cran = "pingers" 

	version("0.1.1", md5="6e22b91d4275cfd86c8c720e2183904a")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tictoc", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
