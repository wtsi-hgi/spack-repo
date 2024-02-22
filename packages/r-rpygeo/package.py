# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRpygeo(RPackage):
	"""ArcGIS Geoprocessing via Python

	Provides access to ArcGIS geoprocessing tools by building an 
             interface between R and the ArcPy Python side-package via the 
             reticulate package. 
	"""
	
	homepage = "https://github.com/fapola/RPyGeo"
	cran = "RPyGeo" 

	version("1.0.0", md5="36c0a9d0485ca0d66fcf3d9561e42867")

	depends_on("r-reticulate@1.2:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("python@2.6.0:", type=("build", "link", "run"))
