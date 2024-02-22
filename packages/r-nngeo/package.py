# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNngeo(RPackage):
	"""k-Nearest Neighbor Join for Spatial Data

	K-nearest neighbor search for projected and non-projected 'sf' spatial layers. Nearest neighbor search uses (1) C code from 'GeographicLib' for lon-lat point layers, (2) function knn() from package 'nabor' for projected point layers, or (3) function st_distance() from package 'sf' for line or polygon layers. The package also includes several other utility functions for spatial analysis.
	"""
	
	homepage = "https://michaeldorman.github.io/nngeo/"
	cran = "nngeo" 

	version("0.4.7", md5="0d9de48386df9bb2ae88124b0f7be2fa")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-sf@0.6:", type=("build", "run"))
	depends_on("r-nabor", type=("build", "run"))
	depends_on("r-units", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
