# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCyclestreets(RPackage):
	"""Cycle Routing and Data for Cycling Advocacy

	An interface to the cycle routing/data services provided by
    'CycleStreets', a not-for-profit social enterprise and advocacy
    organisation.  The application programming interfaces (APIs) provided
    by 'CycleStreets' are documented at
    (<https://www.cyclestreets.net/api/>).  The focus of this package is
    the journey planning API, which aims to emulate the routes taken by a
    knowledgeable cyclist.  An innovative feature of the routing service
    of its provision of fastest, quietest and balanced profiles.  These
    represent routes taken to minimise time, avoid traffic and compromise
    between the two, respectively.
	"""
	
	homepage = "https://rpackage.cyclestreets.net/"
	cran = "cyclestreets" 

	version("1.0.1", md5="d35994c93a597835b8e2c81902b66685")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-geojsonsf", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-progressr", type=("build", "run"))
	depends_on("r-rcppsimdjson", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
