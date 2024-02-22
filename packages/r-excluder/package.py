# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExcluder(RPackage):
	"""Checks for Exclusion Criteria in Online Data

	Data that are collected through online sources such as
    Mechanical Turk may require excluding rows because of IP address
    duplication, geolocation, or completion duration. This package
    facilitates exclusion of these data for Qualtrics datasets.
	"""
	
	homepage = "https://docs.ropensci.org/excluder/"
	cran = "excluder" 

	version("0.5.1", md5="e8f1ea3d711bc7d15ffc41a227f0e063")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ipaddress", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-maps", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
