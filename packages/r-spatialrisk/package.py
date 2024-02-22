# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpatialrisk(RPackage):
	"""Calculating Spatial Risk

	Methods for spatial risk calculations. It offers an efficient approach to determine the sum of all observations within a 
     circle of a certain radius. This might be beneficial for insurers who are required (by a recent European Commission regulation) to determine 
     the maximum value of insured fire risk policies of all buildings that are partly or fully located within a circle of a radius of 200m. See 
     Church (1974) <doi:10.1007/BF01942293> for a description of the problem.
	"""
	
	homepage = "https://github.com/mharinga/spatialrisk"
	cran = "spatialrisk" 

	version("0.7.1", md5="e944c226363aac841b4ed1fab4435b79")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-classint", type=("build", "run"))
	depends_on("r-colourvalues", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-gensa", type=("build", "run"))
	depends_on("r-geohashtools", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-leafem", type=("build", "run"))
	depends_on("r-leafgl", type=("build", "run"))
	depends_on("r-leaflet", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-tmap", type=("build", "run"))
	depends_on("r-units", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
