# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScrobbler(RPackage):
	"""Download 'Scrobbles' from 'Last.fm'

	'Last.fm'<https://www.last.fm> is a music platform focussed on building a 
    detailed profile of a users listening habits. It does this by 'scrobbling' (recording) 
    every track you listen to on other platforms ('spotify', 'youtube', 'soundcloud' etc)
    and transferring them to your 'Last.fm' database. This allows 'Last.fm' to act as a 
    complete record of your entire listening history. 'scrobbler' provides helper functions
    to download and analyse your listening history in R.
	"""
	
	homepage = "https://github.com/condwanaland/scrobbler"
	cran = "scrobbler" 

	version("1.0.3", md5="13b81786e071e4c9a9108667551577a3")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
