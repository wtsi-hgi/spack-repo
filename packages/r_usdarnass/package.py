# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUsdarnass(RPackage):
	"""USDA NASS Quick Stats API

	An alternative for downloading various United States Department of
    Agriculture (USDA) data from <https://quickstats.nass.usda.gov/> through R. 
    You must sign up for an API token from the mentioned website in order for 
    this package to work.
	"""
	
	homepage = "https://github.com/rdinter/usdarnass"
	cran = "usdarnass" 

	version("0.1.0", md5="4fb78b55f2bb80f278ec8b668a25655c")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
