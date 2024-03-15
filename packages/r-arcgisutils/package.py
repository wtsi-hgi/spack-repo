# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArcgisutils(RPackage):
	"""ArcGIS Utility Functions

	Developer oriented utility functions designed to be used as
    the building blocks of R packages that work with ArcGIS Location
    Services. It provides functionality for authorization, Esri JSON
    construction and parsing, as well as other utilities pertaining to
    geometry and Esri type conversions. To support 'ArcGIS Pro' users,
    authorization can be done via 'arcgisbinding'. Installation
    instructions for 'arcgisbinding' can be found at
    <https://r.esri.com/r-bridge-site/arcgisbinding/installing-arcgisbinding.html>.
	"""
	
	homepage = "https://github.com/R-ArcGIS/arcgisutils"
	cran = "arcgisutils" 

	version("0.2.0", md5="04ec44f6b1462fa2f988266e066b34b5")

	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dbplyr", type=("build", "run"))
	depends_on("r-httr2@1:", type=("build", "run"))
	depends_on("r-jsonify", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppsimdjson", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
