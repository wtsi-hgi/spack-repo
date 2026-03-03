# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNoaastormevents(RPackage):
	"""Explore NOAA Storm Events Database

	Allows users to explore and plot data from the
    National Oceanic and Atmospheric Administration (NOAA) 
    Storm Events database through R for United States counties. 
    Functionality includes matching storm event listings by time and 
    location to hurricane best tracks data. This work was 
    supported by grants from the Colorado Water Center, the National Institute 
    of Environmental Health Sciences (R00ES022631) and the National Science 
    Foundation (1331399). 
	"""
	
	homepage = "https://github.com/geanders/noaastormevents"
	cran = "noaastormevents" 

	version("0.2.0", md5="7f82615f53625a9f2439a4369d63acd2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-choroplethr@3.7:", type=("build", "run"))
	depends_on("r-choroplethrmaps@1.0.1:", type=("build", "run"))
	depends_on("r-data-table@1.13:", type=("build", "run"))
	depends_on("r-dplyr@1.0.2:", type=("build", "run"))
	depends_on("r-forcats@0.5:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.2:", type=("build", "run"))
	depends_on("r-hurricaneexposure@0.1.1:", type=("build", "run"))
	depends_on("r-lubridate@1.7.9:", type=("build", "run"))
	depends_on("r-maps@3.3:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-plyr@1.8.6:", type=("build", "run"))
	depends_on("r-rcolorbrewer@1.1.2:", type=("build", "run"))
	depends_on("r-rcurl@1.98.1.2:", type=("build", "run"))
	depends_on("r-rlang@0.4.7:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-tibble@3.0.3:", type=("build", "run"))
	depends_on("r-tidyr@1.1.1:", type=("build", "run"))
	depends_on("r-viridis@0.5.1:", type=("build", "run"))
	depends_on("r-xml@3.99.0.3:", type=("build", "run"))
