# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBgganalytics(RPackage):
	"""BoardGameGeek's Board Game Data Analysis Tools

	Tools for analysing board game data. Mainly focused on providing 
    an interface for BoardGameGeek's XML API2 through R6 class system objects.
    More details about the BoardGameGeek's API can be obtained here
    <https://boardgamegeek.com/wiki/page/BGG_XML_API2>.
	"""
	
	homepage = "https://github.com/JakubBujnowicz/bggAnalytics"
	cran = "bggAnalytics" 

	version("0.2.1", md5="d8ab61fefc43b17b3c688cfe1793c7ab")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-pryr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
