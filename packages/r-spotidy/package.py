# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpotidy(RPackage):
	"""Providing Convenience Functions to Connect R with the Spotify
API

	Providing convenience functions to connect R with the 'Spotify' application programming interface ('API'). At first it aims to help setting up 
  the OAuth2.0 Authentication flow. The default output of the get_*() functions is tidy, but optionally the functions could return the raw response from the 
  'API' as well. The search_*() and get_*() functions can be combined. See the vignette for more information and examples and the official Spotify for 
  Developers website <https://developer.spotify.com/documentation/web-api/> for information about the Web 'API'.
	"""
	
	cran = "spotidy" 

	version("0.1.0", md5="a283dfc75b77a75576771394689329be")

	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
