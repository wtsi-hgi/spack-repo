# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsaga(RPackage):
	"""SAGA Geoprocessing and Terrain Analysis

	Provides access to geocomputing and terrain analysis functions
    of the geographical information system (GIS) 'SAGA' (System for Automated
    Geoscientific Analyses) from within R by running the command line version of
    SAGA. This package furthermore provides several R functions for handling ASCII
    grids, including a flexible framework for applying local functions (including
    predict methods of fitted models) and focal functions to multiple grids. SAGA
    GIS is available under GPL-2 / LGPL-2 licences from 
    <https://sourceforge.net/projects/saga-gis/>.
	"""
	
	homepage = "https://github.com/r-spatial/RSAGA"
	cran = "RSAGA" 

	version("1.4.0", md5="9d29e3853bbe527fb2c2d68209afaf27")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-gstat", type=("build", "run"))
	depends_on("r-shapefiles", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("saga-gis@2.3:", type=("build", "link", "run"))
