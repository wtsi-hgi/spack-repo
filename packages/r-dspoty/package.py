# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDspoty(RPackage):
	"""Get 'Spotify' API Multiple Information

	You can retrieve 'Spotify' API Information such as artists, albums, tracks, features tracks, recommendations or related artists.
    This package allows you to search all the information by name and also includes a distance based algorithm to find similar songs.
	More information: <https://developer.spotify.com/documentation/web-api/> .
	"""
	
	homepage = "https://github.com/AlbertoAlmuinha/DSpoty"
	cran = "DSpoty" 

	version("0.1.0", md5="a86e88b9065804ee1fb18048b8daf88e")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
