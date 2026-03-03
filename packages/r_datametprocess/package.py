# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDatametprocess(RPackage):
	"""Meteorological Data Processing

	Set of tools aimed at processing meteorological data, converting hourly recorded data to daily, monthly and annual data.
	"""
	
	cran = "DataMetProcess" 

	version("1.0.1", md5="18487959f8a941ddf4c893ec29f7a51b")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
