# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCcamlrgis(RPackage):
	"""Antarctic Spatial Data Manipulation

	Loads and creates spatial data, including layers and tools that are relevant
    to the activities of the Commission for the Conservation of Antarctic Marine Living 
    Resources. Provides two categories of functions: load functions and create functions.
    Load functions are used to import existing spatial layers from the online CCAMLR GIS
    such as the ASD boundaries. Create functions are used to create layers from user data
    such as polygons and grids.
	"""
	
	homepage = "https://github.com/ccamlr/CCAMLRGIS#table-of-contents"
	cran = "CCAMLRGIS" 

	version("4.0.7", md5="c625f0d1dbc9d278975be208af380774")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-stars", type=("build", "run"))
	depends_on("r-bezier", type=("build", "run"))
	depends_on("r-lwgeom", type=("build", "run"))
