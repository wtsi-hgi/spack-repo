# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTinyspotifyr(RPackage):
	"""Tinyverse R Wrapper for the 'Spotify' Web API

	An R wrapper for the 'Spotify' Web API 
  <https://developer.spotify.com/web-api/>.
	"""
	
	homepage = "https://github.com/TroyHernandez/tinyspotifyr"
	cran = "tinyspotifyr" 

	version("0.2.2", md5="29f82e89f85b953cd3d460ec75775eee")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
