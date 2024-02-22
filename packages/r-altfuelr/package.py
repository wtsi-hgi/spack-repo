# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAltfuelr(RPackage):
	"""Provides an Interface to the NREL Alternate Fuels Locator

	Provides a number of functions to access the 
    National Energy Research Laboratory Alternate Fuel Locator API 
    <https://developer.nrel.gov/docs/transportation/alt-fuel-stations-v1/>. 
    The Alternate Fuel Locator shows the location of alternate fuel stations in the United States 
    and Canada. This package also includes the data from the US Department of Energy Alternate Fuel
    database as a data set.
	"""
	
	cran = "altfuelr" 

	version("0.1.0", md5="b264b45578ef821922468000221ba603")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
