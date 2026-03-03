# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDatastreamdsws2r(RPackage):
	"""Provides a Link Between the 'Refinitiv Datastream' System and R

	Provides a set of functions and a class to connect, extract and
    upload information from the 'Refinitiv Datastream' database. This
    package uses the 'DSWS' API and server used by the 'Datastream DFO addin'.  
    Details of this API are available at <https://www.lseg.com/en/data-analytics>.
    Please report issues at <https://github.com/CharlesCara/DatastreamDSWS2R/issues>.
	"""
	
	cran = "DatastreamDSWS2R" 

	version("1.9.7", md5="23d2401a87d0b7fab25b9d05c8e81cce")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
