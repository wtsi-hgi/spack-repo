# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROpenmeteo(RPackage):
	"""Retrieve Weather Data from the Open-Meteo API

	A client for the Open-Meteo API that retrieves Open-Meteo
    weather data in a tidy format. No API key is required. The API specification
    is located at <https://open-meteo.com/en/docs>.
	"""
	
	cran = "openmeteo" 

	version("0.2.4", md5="5557ec8231db15a06726011d77bfde2f")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tibblify", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-testthat@3:", type=("build", "run"))
