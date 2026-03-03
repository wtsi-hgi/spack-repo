# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExtratum(RPackage):
	"""Summary Statistics for Geospatial Features

	Provides summary statistics of local geospatial features within a given geographic area. 
	It does so by calculating the area covered by a target geospatial feature (i.e. buildings, parks, lakes, etc.). 
	The geospatial features can be of any type of geospatial data, including point, polygon or line data.
	"""
	
	cran = "extRatum" 

	version("1.0.4", md5="a8964311af06b2c60ac385f6d0e2abc6")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-sf@0.9.5:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-tidyr@1.1:", type=("build", "run"))
	depends_on("gdal@2.0.1:", type=("build", "link", "run"))
	depends_on("geos@3.4.0:", type=("build", "link", "run"))
	depends_on("proj@4.8.0:", type=("build", "link", "run"))
