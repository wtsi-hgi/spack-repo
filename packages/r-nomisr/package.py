# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNomisr(RPackage):
	"""Access 'Nomis' UK Labour Market Data

	Access UK official statistics from the 'Nomis' database. 
    'Nomis' includes data from the Census, the Labour Force Survey, DWP benefit 
    statistics and other economic and demographic data from the Office for 
    National Statistics, based around statistical geographies. See 
    <https://www.nomisweb.co.uk/api/v01/help> for full API documentation.
	"""
	
	homepage = "https://github.com/ropensci/nomisr"
	cran = "nomisr" 

	version("0.4.7", md5="e3698ae67738e3215c21928d0ca243ef")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-rsdmx", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-snakecase", type=("build", "run"))
