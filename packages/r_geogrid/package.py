# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeogrid(RPackage):
	"""Turn Geospatial Polygons into Regular or Hexagonal Grids

	Turn irregular polygons (such as geographical regions) into regular or hexagonal grids.
    This package enables the generation of regular (square) and hexagonal grids through the package 
    'sp' and then assigns the content of the existing polygons to the new grid using 
    the Hungarian algorithm, Kuhn (1955) (<doi:10.1007/978-3-540-68279-0_2>). 
    This prevents the need for manual generation of hexagonal grids or regular grids 
    that are supposed to reflect existing geography.
	"""
	
	homepage = "https://github.com/jbaileyh/geogrid"
	cran = "geogrid" 

	version("0.1.2", md5="8791562d156b4f9e9b338c1947e496e3")

	depends_on("r-sp", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
