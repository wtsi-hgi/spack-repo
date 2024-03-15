# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeouy(RPackage):
	"""Geographic Information of Uruguay

	The toolbox have functions to load and process geographic
    information for Uruguay.  And extra-function to get address
    coordinates and orthophotos through the uruguayan 'IDE' API
    <https://www.gub.uy/infraestructura-datos-espaciales/tramites-y-servicios/servicios/sistema-unico-direcciones-geograficas>.
	"""
	
	cran = "geouy" 

	version("0.2.8", md5="368ec16c4a04e49d6cea47cfeee614dc")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggspatial", type=("build", "run"))
	depends_on("r-ggthemes", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("unrar", type=("build", "link", "run"))
	depends_on("gdal@2.0.1:", type=("build", "link", "run"))
	depends_on("geos@3.8.0:", type=("build", "link", "run"))
	depends_on("proj@6.2.1", type=("build", "link", "run"))
