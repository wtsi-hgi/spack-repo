# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimet(RPackage):
	"""Tools for Simulation of Evapotranspiration of Field Crops and
Soil Water Balance

	Supports the calculation of meteorological characteristics in 
      evapotranspiration research and reference crop evapotranspiration, and offers 
      three models to simulate crop evapotranspiration and soil water balance in 
      the field, including single crop coefficient and dual crop coefficient, 
      as well as the Shuttleworth-Wallace model. These calculations main refer to 
      Allen et al.(1998, ISBN:92-5-104219-5), Teh (2006, ISBN:1-58-112-998-X), and 
      Liu et al.(2006) <doi:10.1016/j.agwat.2006.01.018>.
	"""
	
	cran = "simET" 

	version("1.0.3", md5="5aefe117f6108f173f1b743fd83dad16")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpmisc", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
