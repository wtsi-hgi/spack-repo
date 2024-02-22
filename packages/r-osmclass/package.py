# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROsmclass(RPackage):
	"""Classify Open Street Map Features

	Classify Open Street Map (OSM) features into meaningful functional 
    or analytical categories. Designed for OSM PBF files, e.g. from <https://download.geofabrik.de/> 
    imported as spatial data frames. A classification consists of a list of categories that are related to 
    certain OSM tags and values. Given a layer from an OSM PBF file and a classification, the main 
    osm_classify() function returns a classification data table giving, for each feature, the primary and 
    alternative categories (if there is overlap) assigned, and the tag(s) and value(s) matched on. 
    The package also contains a classification of OSM features by economic function/significance, 
    following Krantz (2023) <https://www.ssrn.com/abstract=4537867>.
	"""
	
	cran = "osmclass" 

	version("0.1.3", md5="f99275e0399c82108e9c50d286ca1770")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-collapse@1.9.6:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
