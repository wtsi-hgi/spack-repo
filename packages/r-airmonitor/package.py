# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAirmonitor(RPackage):
	"""Air Quality Data Analysis

	Utilities for working with hourly air quality monitoring data
    with a focus on small particulates (PM2.5). A compact data model is 
    structured as a list with two dataframes. A 'meta' dataframe contains 
    spatial and measuring device metadata associated with deployments at known 
    locations. A 'data' dataframe contains a 'datetime' column followed by 
    columns of measurements associated with each "device-deployment".
    Algorithms to calculate NowCast and the associated Air Quality Index (AQI)
    are defined at the US Environmental Projection Agency AirNow program:
    <https://www.airnow.gov/sites/default/files/2020-05/aqi-technical-assistance-document-sept2018.pdf>.
	"""
	
	homepage = "https://github.com/MazamaScience/AirMonitor"
	cran = "AirMonitor" 

	version("0.4.0", md5="4cd1b6c3f5b07947056feec134a4ba60")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dygraphs", type=("build", "run"))
	depends_on("r-leaflet", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mazamacoreutils@0.5.2:", type=("build", "run"))
	depends_on("r-mazamarollutils@0.1.3:", type=("build", "run"))
	depends_on("r-mazamatimeseries@0.2.16:", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
