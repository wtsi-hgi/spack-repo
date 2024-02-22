# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsinaica(RPackage):
	"""Download Data from Mexico's Air Quality Information System

	Easy-to-use functions for downloading air quality data from
    the Mexican National Air Quality Information System (SINAICA).  Allows
    you to query pollution and meteorological parameters from more than a
    hundred monitoring stations located throughout Mexico. See
    <https://sinaica.inecc.gob.mx> for more information.
	"""
	
	homepage = "https://hoyodesmog.diegovalle.net/rsinaica/"
	cran = "rsinaica" 

	version("1.0.0", md5="e35da659492243b134e91f1f068509c0")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
