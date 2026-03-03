# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTabularmaps(RPackage):
	"""Create Tile-Grid Geographical Maps

	The 'tabularmap' is one of the visualization methods for 
    efficiently displaying data consisting of multiple elements by tiling them.
    When dealing with geospatial, it corrects for differences in visibility 
    between areas.
	"""
	
	homepage = "https://github.com/uribo/tabularmaps"
	cran = "tabularmaps" 

	version("0.1.0", md5="8a54deeef8496991bc04d90efcdc1730")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-ggforce@0.3.2:", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-rlang@0.4.7:", type=("build", "run"))
