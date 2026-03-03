# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeoar(RPackage):
	"""Argentina's Spatial Data Toolbox

	Collection of tools that facilitates data access and workflow for spatial analysis of Argentina. Includes historical information from censuses, administrative limits at different levels of aggregation, location of human settlements, among others. Since it is expected that the majority of users will be Spanish-speaking, the documentation of the package prioritizes this language, although an effort is made to also offer annotations in English. 
	"""
	
	homepage = "https://github.com/PoliticaArgentina/geoAr"
	cran = "geoAr" 

	version("1.0.0", md5="06db4255fc02c1f410f541ac24bbe518")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-attempt", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-leaflet", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
