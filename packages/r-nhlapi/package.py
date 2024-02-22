# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNhlapi(RPackage):
	"""A Minimum-Dependency 'R' Interface to the 'NHL' API

	Retrieves and processes the data exposed by the open 'NHL' API. This includes information on players, teams, games, tournaments, drafts, standings, schedules and other endpoints. A lower-level interface to access the data via URLs directly is also provided.
	"""
	
	homepage = "https://github.com/jozefhajnala/nhlapi"
	cran = "nhlapi" 

	version("0.1.4", md5="fd52f9eade341929abe505b5af1de980")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
