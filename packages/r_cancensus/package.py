# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCancensus(RPackage):
	"""Access, Retrieve, and Work with Canadian Census Data and
Geography

	Integrated, convenient, and uniform access to Canadian
    Census data and geography retrieved using the 'CensusMapper' API. This package produces analysis-ready 
    tidy data frames and spatial data in multiple formats, as well as convenience functions
    for working with Census variables, variable hierarchies, and region selection. API
    keys are freely available with free registration at <https://censusmapper.ca/api>.
    Census data and boundary geometries are reproduced and distributed on an "as
    is" basis with the permission of Statistics Canada (Statistics Canada 2001; 2006;
    2011; 2016; 2021).
	"""
	
	homepage = "https://github.com/mountainMath/cancensus"
	cran = "cancensus" 

	version("0.5.7", md5="db5f3191049c6182d62e63a85237e40e")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-digest@0.1:", type=("build", "run"))
	depends_on("r-dplyr@0.7:", type=("build", "run"))
	depends_on("r-httr@1:", type=("build", "run"))
	depends_on("r-jsonlite@1:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
