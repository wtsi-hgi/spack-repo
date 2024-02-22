# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBangladesh(RPackage):
	"""Provides Ready to Use Shapefiles for Geographical Map of
Bangladesh

	Usually, it is difficult to plot choropleth maps for Bangladesh in 'R'.
    The 'bangladesh' package provides ready-to-use shapefiles for different administrative
    regions of Bangladesh (e.g., Division, District, Upazila, and Union).
    This package helps users to draw thematic maps of administrative regions
    of Bangladesh easily as it comes with the 'sf' objects for the boundaries.
    It also provides functions allowing users to efficiently get specific area
    maps and center coordinates for regions. Users can also search for
    a specific area and calculate the centroids of those areas.
	"""
	
	cran = "bangladesh" 

	version("1.0.0", md5="389804cc800016b37058111dff34e4ce")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-tmap", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
