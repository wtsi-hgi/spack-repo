# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRzentra(RPackage):
	"""Client for the 'ZENTRA Cloud' API

	Provides functionality to read settings, statuses and readings of
  weather stations from the 'ZENTRA Cloud' API 
  <https://zentracloud.com/api/v1/guide#APIGuidelines>. 
	"""
	
	cran = "rzentra" 

	version("0.1.0", md5="8e77fede2de86a3765856753319c956e")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
