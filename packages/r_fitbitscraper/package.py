# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFitbitscraper(RPackage):
	"""Scrapes Data from Fitbit

	Scrapes data from Fitbit <http://www.fitbit.com>. This does not use the official
    API, but instead uses the API that the web dashboard uses to generate the graphs
    displayed on the dashboard after login at <http://www.fitbit.com>.
	"""
	
	homepage = "https://github.com/corynissen/fitbitScraper"
	cran = "fitbitScraper" 

	version("0.1.8", md5="f683ac3ec597e5c05500f9553455c94b")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
