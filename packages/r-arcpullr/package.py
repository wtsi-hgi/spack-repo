# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArcpullr(RPackage):
	"""Pull Data from an 'ArcGIS REST' API

	
  Functions to efficiently query 'ArcGIS REST' APIs 
  <https://developers.arcgis.com/rest/>. 
  Both spatial and SQL queries can be used to retrieve data. 
  Simple Feature (sf) objects are utilized to perform spatial queries. 
  This package was neither produced nor is maintained by Esri.
	"""
	
	cran = "arcpullr" 

	version("0.2.8", md5="2fa9f82ead4304da815ead3013780a8b")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-sf@0.9.7:", type=("build", "run"))
	depends_on("r-httr@1.4.1:", type=("build", "run"))
	depends_on("r-jsonlite@1.6.1:", type=("build", "run"))
	depends_on("r-dplyr@1.0.2:", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-tidyr@1.0.2:", type=("build", "run"))
	depends_on("r-rlang@0.4.7:", type=("build", "run"))
	depends_on("r-raster@3.4.5:", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
