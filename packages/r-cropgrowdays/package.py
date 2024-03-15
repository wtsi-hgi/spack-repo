# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCropgrowdays(RPackage):
	"""Crop Growing Degree Days and Agrometeorological Calculations

	Calculate agrometeorological variables for crops
             including growing degree days (McMaster, GS & Wilhelm, WW
             (1997) <doi:10.1016/S0168-1923(97)00027-0>), cumulative
             rainfall, number of stress days and cumulative or mean
             radiation and evaporation. Convert dates to day of year
             and vice versa. Also, download curated and interpolated
             Australian weather data from the Queensland Government
             DES longpaddock website
             <https://www.longpaddock.qld.gov.au/>. This data is
             freely available under the Creative Commons 4.0 licence.
	"""
	
	homepage = "https://gitlab.com/petebaker/cropgrowdays/"
	cran = "cropgrowdays" 

	version("0.2.1", md5="2c976ff324b9332d1f55dabe43184af4")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-purrrlyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
