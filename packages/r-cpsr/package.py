# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCpsr(RPackage):
	"""Load CPS Microdata into R Using the 'Census Bureau Data' API

	Load Current Population Survey (CPS) microdata into R using the
    'Census Bureau Data' API
    (<https://www.census.gov/data/developers/data-sets.html>), including basic
    monthly CPS and CPS ASEC microdata.
	"""
	
	homepage = "https://github.com/matt-saenz/cpsR"
	cran = "cpsR" 

	version("1.0.0", md5="8e97531b26ee132bfba3d7ef62141422")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
