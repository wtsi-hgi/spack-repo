# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAireZmvm(RPackage):
	"""Download Mexico City Pollution, Wind, and Temperature Data

	Tools for downloading hourly averages, daily maximums and
    minimums from each of the pollution, wind, and temperature measuring
    stations or geographic zones in the Mexico City metro area. The
    package also includes the locations of each of the stations and zones.
    See <http://aire.cdmx.gob.mx/> for more information.
	"""
	
	homepage = "https://hoyodesmog.diegovalle.net/aire.zmvm/"
	cran = "aire.zmvm" 

	version("0.9.0", md5="8dde831eeb34757b8d5660b0de319afc")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
