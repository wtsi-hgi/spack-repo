# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMicromapst(RPackage):
	"""Linked Micromap Plots for U. S. and Other Geographic Areas

	Provides the users with the ability to quickly create
     linked micromap plots for a collection of geographic areas.
     Linked micromap plots are visualizations of geo-referenced data
     that link statistical graphics to an organized series of small
     maps or graphic images. The Help description contains examples
     of how to use the 'micromapST' function. Contained in this
     package are border group datasets to support creating linked
     micromap plots for the 50 U.S. states and District of Columbia
     (51 areas), the U. S. 20 Seer Registries, the 105 counties in
     the state of Kansas, the 62 counties of New York, the 24
     counties of Maryland, the 29 counties of Utah, the 32
     administrative areas in China, the 218 administrative areas in
     the UK and Ireland (for testing only), the 25 districts in the
     city of Seoul South Korea, and the 52 counties on the Africa
     continent.
     A border group dataset contains the boundaries related to the
     data level areas, a second layer boundaries, a top or third
     layer boundary, a parameter list of run options, and a cross
     indexing table between area names, abbreviations, numeric
     identification and alias matching strings for the specific
     geographic area.  By specifying a border group, the package
     create linked micromap plots for any geographic region.  The
     user can create and provide their own border group dataset for
     any area beyond the areas contained within the package. In version 3.0.0,
     the 'BuildBorderGroup' function was upgraded to not use the retiring
     'maptools', 'rgdal', and 'rgeos' packages. 
     References: Carr and Pickle, Chapman and Hall/CRC, Visualizing
     Data Patterns with Micromaps, CRC Press, 2010. Pickle, Pearson,
     and Carr (2015), micromapST: Exploring and Communicating
     Geospatial Patterns in US State Data., Journal of Statistical
     Software, 63(3), 1-25., <https://www.jstatsoft.org/v63/i03/>.
     Copyrighted 2013, 2014, 2015, 2016, 2022, 2023, and 2024 by Carr, Pearson
     and Pickle.
	"""
	
	cran = "micromapST" 

	version("3.0.2", md5="dd5fc9045a87fd3da09994ff4a3f8d34")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-labeling", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-spdep", type=("build", "run"))
	depends_on("r-rmapshaper", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-writexl", type=("build", "run"))
