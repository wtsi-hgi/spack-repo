# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZctacrosswalk(RPackage):
	"""Crosswalk Between 2020 Census ZIP Code Tabulation Areas (ZCTAs),
States and Counties

	Contains the US Census Bureau's 2020 ZCTA to County Relationship 
    File, as well as convenience functions to translate between States, Counties
    and ZIP Code Tabulation Areas (ZCTAs).
	"""
	
	homepage = "https://github.com/MarketBridge/zctaCrosswalk"
	cran = "zctaCrosswalk" 

	version("2.0.0", md5="0debd53ce8547eab167878498f1a91c0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
