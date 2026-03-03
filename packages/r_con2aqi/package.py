# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCon2aqi(RPackage):
	"""Calculate the AQI from Pollutant Concentration

	To calculate the AQI (Air Quality Index) from pollutant concentration data.
    O3, PM2.5, PM10, CO, SO2, and NO2 are available currently.
    The method can be referenced at Environmental Protection Agency, United States as follows:
    EPA (2016) <https://www3.epa.gov/airnow/aqi-technical-assistance-document-may2016.pdf>.
	"""
	
	cran = "con2aqi" 

	version("0.1.0", md5="26dbf881850a593a12a98c7845e42c64")

