# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeogenr(RPackage):
	"""Generator from American Community Survey Geodatabases

	The American Community Survey (ACS)
    <https://www.census.gov/programs-surveys/acs> offers geodatabases with
    geographic information and associated data of interest to researchers
    in the area. The goal of this package is to generate objects that
    allow us to access and consult the information available in various
    formats, such as in 'GeoPackage' format or in multidimensional 'ROLAP'
    (Relational On-Line Analytical Processing) star format.
	"""
	
	homepage = "https://josesamos.github.io/geogenr/"
	cran = "geogenr" 

	version("2.0.1", md5="0236009fae4c3237457ab663efcbe5c5")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-geomultistar", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rolap", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
