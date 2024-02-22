# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSungeo(RPackage):
	"""Sub-National Geospatial Data Archive: Geoprocessing Toolkit

	Tools for integrating spatially-misaligned GIS datasets. Part of the Sub-National Geospatial Data Archive System.
	"""
	
	homepage = "<https://github.com/zhukovyuri/SUNGEO>"
	cran = "SUNGEO" 

	version("1.2.1", md5="438d6507c9f556cd28abdceae494d01e")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-measurements", type=("build", "run"))
	depends_on("r-rann", type=("build", "run"))
	depends_on("r-cartogram", type=("build", "run"))
	depends_on("r-packcircles", type=("build", "run"))
	depends_on("r-rmapshaper", type=("build", "run"))
	depends_on("r-spdep", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-automap", type=("build", "run"))
