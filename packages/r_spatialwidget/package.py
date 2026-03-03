# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpatialwidget(RPackage):
	"""Formats Spatial Data for Use in Htmlwidgets

	Many packages use 'htmlwidgets' <https://CRAN.R-project.org/package=htmlwidgets>
    for interactive plotting of spatial data.
    This package provides functions for converting R objects, such as simple features, 
    into structures suitable for use in 'htmlwidgets' mapping libraries. 
	"""
	
	homepage = "https://symbolixau.github.io/spatialwidget/articles/spatialwidget.html"
	cran = "spatialwidget" 

	version("0.2.5", md5="0a2240181b0a04fe45fae61e73fd1345")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rcpp@0.12.18:", type=("build", "run"))
	depends_on("r-bh@1.84:", type=("build", "run"))
	depends_on("r-colourvalues@0.3.9:", type=("build", "run"))
	depends_on("r-geojsonsf@2.0.3:", type=("build", "run"))
	depends_on("r-geometries@0.2.4:", type=("build", "run"))
	depends_on("r-interleave@0.1.2:", type=("build", "run"))
	depends_on("r-jsonify@1.2.2:", type=("build", "run"))
	depends_on("r-rapidjsonr", type=("build", "run"))
	depends_on("r-sfheaders@0.4.4:", type=("build", "run"))
