# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStationary(RPackage):
	"""Detailed Meteorological Data from Stations All Over the World

	Acquire hourly meteorological data from stations located all over
    the world. There is a wealth of data available, with historic weather data
    accessible from nearly 30,000 stations. The available data is automatically
    downloaded from a data repository and processed into a 'tibble' for the
    exact range of years requested. A relative humidity approximation is
    provided using the 'August-Roche-Magnus' formula, which was adapted from
    Alduchov and Eskridge (1996) <doi:10.1175%2F1520-0450%281996%29035%3C0601%3AIMFAOS%3E2.0.CO%3B2>.
	"""
	
	homepage = "https://github.com/rich-iannone/stationaRy"
	cran = "stationaRy" 

	version("0.5.1", md5="fe7fb68d3c6548765864dfa5961df1e2")

	depends_on("r@3.2.1:", type=("build", "run"))
	depends_on("r-dplyr@0.8.3:", type=("build", "run"))
	depends_on("r-readr@1.3.1:", type=("build", "run"))
	depends_on("r-downloader@0.4:", type=("build", "run"))
	depends_on("r-lubridate@1.7.4:", type=("build", "run"))
	depends_on("r-lutz@0.3.1:", type=("build", "run"))
	depends_on("r-progress@1.2.2:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-tidyr@0.8.3:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
