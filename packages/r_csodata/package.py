# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCsodata(RPackage):
	"""Download Data from the CSO 'PxStat' API

	Imports 'PxStat' data in JSON-stat format and (optionally) reshapes it into wide
	format. The Central Statistics Office (CSO) is the national statistical institute of Ireland
	and 'PxStat' is the CSOs online database of Official Statistics. This database contains current
	and historical data series compiled from CSO statistical releases and is accessed at
	<http://data.cso.ie>.
	The CSO 'PxStat' Application Programming Interface (API), which is accessed in this package, provides
	access to 'PxStat' data in JSON-stat format at <http://data.cso.ie>.
	This dissemination tool allows developers machine to machine access to CSO 'PxStat' data.
	"""
	
	cran = "csodata" 

	version("1.4.2", md5="e380af358a5b3d244d32f686093291a9")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rjstat", type=("build", "run"))
	depends_on("r-r-cache", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
