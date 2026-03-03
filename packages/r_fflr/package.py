# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFflr(RPackage):
	"""Retrieve ESPN Fantasy Football Data

	Format the raw data from the ESPN fantasy football API
    <https://fantasy.espn.com/apis/v3/games/ffl/> as data frames.
    Retrieve data on public leagues, rosters, athletes, and matches.
	"""
	
	homepage = "https://k5cents.github.io/fflr/"
	cran = "fflr" 

	version("2.2.4", md5="4c077c0bf716487b85bf959562800cc1")
	version("2.2.3", md5="ff28f3b8342a6ecd7950e9ff87433fbe")
	version("2.2.2", md5="d8a76cdf108b806dac99133001218515")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-httr@1.4.7:", type=("build", "run"))
	depends_on("r-jsonlite@1.8.7:", type=("build", "run"))
	depends_on("r-tibble@3.2.1:", type=("build", "run"))
