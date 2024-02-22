# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHansard(RPackage):
	"""Provides Easy Downloading Capabilities for the UK Parliament API

	Provides functions to download data from the 
  <http://www.data.parliament.uk/> APIs. Because of the structure of the API, 
  there is a named function for each type of available data for ease of use, 
  as well as some functions designed to retrieve specific pieces of commonly 
  used data. Functions for each new API will be added as and when they become
  available.
	"""
	
	homepage = "https://docs.evanodell.com/hansard"
	cran = "hansard" 

	version("0.8.0", md5="c8c6b6e47430e82587e30fafdb1961f2")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-snakecase", type=("build", "run"))
