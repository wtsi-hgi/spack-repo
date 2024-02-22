# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClifro(RPackage):
	"""Easily Download and Visualise Climate Data from CliFlo

	CliFlo is a web portal to the New Zealand National Climate
    Database and provides public access (via subscription) to around 6,500
    various climate stations (see <https://cliflo.niwa.co.nz/> for more
    information). Collating and manipulating data from CliFlo
    (hence clifro) and importing into R for further analysis, exploration and
    visualisation is now straightforward and coherent. The user is required to
    have an internet connection, and a current CliFlo subscription (free) if
    data from stations, other than the public Reefton electronic weather
    station, is sought.
	"""
	
	homepage = "https://docs.ropensci.org/clifro/"
	cran = "clifro" 

	version("3.2-5", md5="4832ef41e2db3118e44918e44071f6a5")

	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-ggplot2@2:", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
