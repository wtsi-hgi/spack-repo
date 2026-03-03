# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnrfa(RPackage):
	"""UK National River Flow Archive Data from R

	Utility functions to retrieve data from the UK National River Flow Archive (<https://nrfa.ceh.ac.uk/>, terms and conditions: <https://nrfa.ceh.ac.uk/costs-terms-and-conditions>). The package contains R wrappers to the UK NRFA data temporary-API. There are functions to retrieve stations falling in a bounding box, to generate a map and extracting time series and general information. The package is fully  described in Vitolo et al (2016) "rnrfa: An R package to Retrieve, Filter and Visualize Data from the UK National River Flow Archive" <https://journal.r-project.org/archive/2016/RJ-2016-036/RJ-2016-036.pdf>.
	"""
	
	homepage = "https://ilapros.github.io/rnrfa/"
	cran = "rnrfa" 

	version("2.1.0.5", md5="c3c04e9f393e6119b5f3f386fc80a4a3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-ggmap@4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
