# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRiem(RPackage):
	"""Accesses Weather Data from the Iowa Environment Mesonet

	Allows to get weather data from Automated Surface Observing
    System (ASOS) stations (airports) in the whole world thanks to the
    Iowa Environment Mesonet website.
	"""
	
	homepage = "https://docs.ropensci.org/riem/"
	cran = "riem" 

	version("0.3.0", md5="53763ad5125fa90a0c576c19a439d883")

	depends_on("r-httr2", type=("build", "run"))
	depends_on("r-jsonlite@0.9.19:", type=("build", "run"))
	depends_on("r-lubridate@1.5.6:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
