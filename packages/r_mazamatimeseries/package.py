# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMazamatimeseries(RPackage):
	"""Core Functionality for Environmental Time Series

	Utility functions for working with environmental time series data from known 
    locations. The compact data model is structured as a list with two dataframes. A 
    'meta' dataframe contains spatial and measuring device metadata associated with 
    deployments at known locations. A 'data' dataframe contains a 'datetime' column 
    followed by columns of measurements associated with each "device-deployment".
    Ephemerides calculations are based on code originally found in NOAA's
    "Solar Calculator" <https://gml.noaa.gov/grad/solcalc/>.
	"""
	
	homepage = "https://github.com/MazamaScience/MazamaTimeSeries"
	cran = "MazamaTimeSeries" 

	version("0.3.0", md5="a1861d6c8c11885c66eefe54cf5f4a18")
	version("0.2.16", md5="f9693f05ebcebe25fdd06c16aa516438")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-geodist", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mazamacoreutils@0.5.2:", type=("build", "run"))
	depends_on("r-mazamarollutils@0.1.3:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
