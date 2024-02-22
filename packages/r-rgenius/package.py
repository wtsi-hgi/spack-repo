# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgenius(RPackage):
	"""Get 'Genius' API Lyrics

	Download the lyrics of your favorite songs in text and table formats. 
    Also search for related songs or song information.
    More information: <https://docs.genius.com/> .
	"""
	
	homepage = "https://github.com/AlbertoAlmuinha/rgenius"
	cran = "rgenius" 

	version("0.1.0", md5="7ed3a94cbf83056b06469c56fd397a74")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
