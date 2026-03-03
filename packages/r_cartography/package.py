# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCartography(RPackage):
	"""Thematic Cartography

	Create and integrate maps in your R workflow. This package helps 
    to design cartographic representations such as proportional symbols, 
    choropleth, typology, flows or discontinuities maps. It also offers several 
    features that improve the graphic presentation of maps, for instance, map 
    palettes, layout elements (scale, north arrow, title...), labels or legends. 
    See Giraud and Lambert (2017) <doi:10.1007/978-3-319-57336-6_13>.
	"""
	
	homepage = "https://github.com/riatelab/cartography/"
	cran = "cartography" 

	version("3.1.4", md5="9daad23969445d70e886b097b884b9c2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-classint", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
