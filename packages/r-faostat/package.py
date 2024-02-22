# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFaostat(RPackage):
	"""Download Data from the FAOSTAT Database

	Download Data from the FAOSTAT Database of the Food and Agricultural Organization (FAO) of the United Nations.
    A list of functions to download statistics from FAOSTAT (database of the FAO <https://www.fao.org/faostat/>) 
    and WDI (database of the World Bank <https://data.worldbank.org/>), and to perform some harmonization operations.
	"""
	
	homepage = "https://gitlab.com/paulrougieux/faostatpackage"
	cran = "FAOSTAT" 

	version("2.3.0", md5="dba2391c77f3c77b2c9312fd1c1220b2")

	depends_on("r-rjsonio@0.96.0:", type=("build", "run"))
	depends_on("r-plyr@1.7.1:", type=("build", "run"))
	depends_on("r-data-table@1.8.2:", type=("build", "run"))
	depends_on("r-mass@7.3.22:", type=("build", "run"))
	depends_on("r-classint@0.1.19:", type=("build", "run"))
	depends_on("r-labeling@0.1:", type=("build", "run"))
	depends_on("r-httr@1:", type=("build", "run"))
