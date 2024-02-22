# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGalah(RPackage):
	"""Biodiversity Data from the GBIF Node Network

	The Global Biodiversity Information Facility 
    ('GBIF', <https://www.gbif.org>) sources data from an international network
    of data providers, known as 'nodes'. Several of these nodes - the "living 
    atlases" (<https://living-atlases.gbif.org>) - maintain their own web 
    services using software originally developed by the Atlas of Living 
    Australia ('ALA', <https://www.ala.org.au>). 'galah' enables the R community 
    to directly access data and resources hosted by 'GBIF' and its partner nodes.
	"""
	
	homepage = "https://galah.ala.org.au/R/"
	cran = "galah" 

	version("2.0.1", md5="5b471a82a721ae6216ca2ba4941a9e4d")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-glue@1.3.2:", type=("build", "run"))
	depends_on("r-httr2", type=("build", "run"))
	depends_on("r-jsonlite@0.9.8:", type=("build", "run"))
	depends_on("r-lifecycle@1:", type=("build", "run"))
	depends_on("r-potions@0.2:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
