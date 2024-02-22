# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpotifyr(RPackage):
	"""R Wrapper for the 'Spotify' Web API

	An R wrapper for pulling data from the 'Spotify' Web API 
  <https://developer.spotify.com/documentation/web-api/> in bulk, or post items on a
  'Spotify' user's playlist.
	"""
	
	homepage = "https://github.com/charlie86/spotifyr"
	cran = "spotifyr" 

	version("2.2.4", md5="181ee49e2e0deb28dbd56a73b11ebd0f")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
