# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRetrosheet(RPackage):
	"""Import Professional Baseball Data from 'Retrosheet'

	A collection of tools to import and structure the (currently) single-season
    event, game-log, roster, and schedule data available from <https://www.retrosheet.org>.
    In particular, the event (a.k.a. play-by-play) files can be especially difficult to parse.
    This package does the parsing on those files, returning the requested data in the most
    practical R structure to use for sabermetric or other analyses.
	"""
	
	homepage = "https://github.com/colindouglas/retrosheet"
	cran = "retrosheet" 

	version("1.1.6", md5="bae64abf8693d7d1fd6d23f43b55de30")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-xml2@1.2.2:", type=("build", "run"))
	depends_on("r-stringi@0.4.1:", type=("build", "run"))
	depends_on("r-httr@1.4.1:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-rvest@0.3.5:", type=("build", "run"))
