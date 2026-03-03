# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REcocomdp(RPackage):
	"""Tools to Create, Use, and Convert ecocomDP Data

	Work with the Ecological Community Data Design Pattern. 'ecocomDP' 
    is a flexible data model for harmonizing ecological community surveys, in a 
    research question agnostic format, from source data published across 
    repositories, and with methods that keep the derived data up-to-date as the 
    underlying sources change. Described in O'Brien et al. (2021), 
    <doi:10.1016/j.ecoinf.2021.101374>.
	"""
	
	homepage = "https://github.com/EDIorg/ecocomDP"
	cran = "ecocomDP" 

	version("1.3.1", md5="64b8dc6065b2ae37fca5662345920ae1")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-eml@2.0.5:", type=("build", "run"))
	depends_on("r-emld@0.5.1:", type=("build", "run"))
	depends_on("r-geosphere", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-neonutilities@2.1.1:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-uuid", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-neonos", type=("build", "run"))
