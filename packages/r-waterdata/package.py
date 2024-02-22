# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWaterdata(RPackage):
	"""Retrieval, Analysis, and Anomaly Calculation of Daily Hydrologic
Time Series Data

	Imports U.S. Geological Survey (USGS) daily hydrologic data from USGS web services (see <https://waterservices.usgs.gov/> for more information), plots the data, addresses some common data problems, and calculates and plots anomalies.    
	"""
	
	homepage = "https://pubs.usgs.gov/of/2012/1168/"
	cran = "waterData" 

	version("1.0.8", md5="fc5c7025721b14d711a6611870e95550")

	depends_on("r@3.2.6:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-latticeextra", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-dataretrieval", type=("build", "run"))
