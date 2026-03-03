# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRspotify(RPackage):
	"""Access to Spotify API

	Provides an interface to the Spotify API <https://developer.spotify.com/documentation/web-api/>.
	"""
	
	cran = "Rspotify" 

	version("0.1.2", md5="d48e3584270f7b7b2ba57de67dcc5c53")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
