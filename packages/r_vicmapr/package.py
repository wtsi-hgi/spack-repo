# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVicmapr(RPackage):
	"""Access Victorian Spatial Data Through Web File Services (WFS)

	Easily interfaces R to spatial datasets available through 
  the Victorian Government's WFS (Web Feature Service): <https://opendata.maps.vic.gov.au/geoserver/ows?request=GetCapabilities&service=wfs>, 
  which allows users to read in 'sf' data from these sources. VicmapR uses the lazy querying approach and code developed by Teucher et al. (2021) for the 'bcdata' R package <doi:10.21105/joss.02927>.
	"""
	
	homepage = "https://justincally.github.io/VicmapR/"
	cran = "VicmapR" 

	version("0.2.3", md5="afe09f51ae31f4b0bd420fff02ca93c8")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-sf@0.8:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-dbplyr@2.2:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-kableextra", type=("build", "run"))
	depends_on("r-mapview", type=("build", "run"))
	depends_on("r-leaflet", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("gdal@3.0.0:", type=("build", "link", "run"))
	depends_on("geos@3.4.0:", type=("build", "link", "run"))
	depends_on("proj@7.0.0:", type=("build", "link", "run"))
