# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGie(RPackage):
	"""API Wrapper for the Natural Gas Transparency Platforms of Gas
Infrastructure Europe

	Providing access to the API for Gas Infrastructure Europe's
    natural gas transparency platforms <https://agsi.gie.eu/> and <https://alsi.gie.eu/>. Lets the user
    easily download metadata on companies and gas storage units covered by
    the API as well as the respective data on regional, country, company
    or facility level.
	"""
	
	cran = "gie" 

	version("0.1.1", md5="010a446d57588059c791343ad3aec9c4")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
