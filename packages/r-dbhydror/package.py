# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDbhydror(RPackage):
	"""'DBHYDRO' Hydrologic and Water Quality Data

	Client for programmatic access to the South Florida Water
  Management District's 'DBHYDRO' database at 
  <https://www.sfwmd.gov/science-data/dbhydro>, with functions
  for accessing hydrologic and water quality data. 
	"""
	
	homepage = "https://github.com/ropensci/dbhydroR"
	cran = "dbhydroR" 

	version("0.2-8", md5="533dfa35892c3a59299b6d074cc80152")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
