# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCruzplot(RPackage):
	"""Plot Shipboard DAS Data

	A utility program oriented to create maps, plot data, and do basic data summaries
    of 'DAS' data <https://swfsc-publications.fisheries.noaa.gov/publications/TM/SWFSC/NOAA-TM-NMFS-SWFSC-305.PDF> 
    produced by 'WinCruz' from the Southwest Fisheries Science Center.
    <https://www.fisheries.noaa.gov/west-coast/science-data/california-current-marine-mammal-assessment-program>.
	"""
	
	homepage = "https://smwoodman.github.io/CruzPlot/"
	cran = "CruzPlot" 

	version("1.4.8", md5="c8a7206af4c43f5e7552d68fb3a97956")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-geosphere", type=("build", "run"))
	depends_on("r-mapdata", type=("build", "run"))
	depends_on("r-marmap", type=("build", "run"))
	depends_on("r-maps", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-swfscdas@0.3:", type=("build", "run"))
