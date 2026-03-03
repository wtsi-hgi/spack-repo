# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRanglapunjab(RPackage):
	"""Displays Palette of 5 Colors

	Displays palette of 5 colors based on photos depicting the unique 
             and vibrant culture of Punjab in Northern India. Since Punjab translates 
             to ``Land of 5 Rivers'' there are 5 colors per palette. If users need 
             more than 5 colors, they can merge 2 to 3 palettes to create their own 
             color-combination, or they can cherry-pick their own custom colors. 
             Users can view up to 3 palettes together. Users can also list all the 
             palette choices. And last but not least, users can see the photo that 
             inspired a particular palette.
	"""
	
	cran = "RanglaPunjab" 

	version("2.3.4", md5="0004885227a14fad682576e59c69d33f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-jpeg", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
