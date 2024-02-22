# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTauturri(RPackage):
	"""Get Data Out of 'Tautulli' (Formerly 'PlexPy')

	'Tautulli' (<http://tautulli.com>) is a monitoring application for 'Plex' Media Servers 
  (<https://www.plex.tv>) which collects a lot of data about media items and server 
  usage such as play counts. This package interacts with the 'Tautulli' API of any 
  specified server to get said data into R. The 'Tautulli' API documentation is available
  at <https://github.com/Tautulli/Tautulli/blob/master/API.md>.
	"""
	
	homepage = "https://github.com/jemus42/tauturri"
	cran = "tauturri" 

	version("0.3.0", md5="6a6d8a1fdcc60565e8ae97bbf7690251")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
