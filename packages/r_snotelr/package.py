# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSnotelr(RPackage):
	"""Calculate and Visualize 'SNOTEL' Snow Data and Seasonality

	Programmatic interface to the 'SNOTEL' snow data
  (<https://www.nrcs.usda.gov/wps/portal/wcc/home>). Provides easy downloads of snow 
  data into your R work space or a local directory. Additional post-processing 
  routines to extract snow season indexes are provided.
	"""
	
	homepage = "https://github.com/bluegreen-labs/snotelr"
	cran = "snotelr" 

	version("1.2", md5="3a20188cea290eed1e0b9f0413b45764")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
