# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGtfstools(RPackage):
	"""General Transit Feed Specification (GTFS) Editing and Analysing
Tools

	Utility functions to read, manipulate, analyse and write
    transit feeds in the General Transit Feed Specification (GTFS) data
    format.
	"""
	
	homepage = "https://ipeagit.github.io/gtfstools/"
	cran = "gtfstools" 

	version("1.2.0", md5="890ec8cff7347f46d18e876fae57cb91")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-gtfsio@1:", type=("build", "run"))
	depends_on("r-processx", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-sfheaders", type=("build", "run"))
	depends_on("r-units", type=("build", "run"))
	depends_on("r-zip", type=("build", "run"))
	depends_on("r-cpp11", type=("build", "run"))
