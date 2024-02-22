# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStppsim(RPackage):
	"""Spatiotemporal Point Patterns Simulation

	Generates artificial spatiotemporal (ST) point patterns
  and/or interactions through the integration of microsimulation 
  (Holm, E., (2017)<doi:10.1002/9781118786352.wbieg0320>) 
  and agent-based models 
  (Bonabeau, E., (2002)<doi:10.1073/pnas.082080899>). 
  The tool enables users to configure the actions of a group of 
  'walkers', which can be agents, objects, individuals, and more. 
  Their engagements with both spatial landscapes (Quaglietta, L. and Porto, M., 
  (2019)<doi:10.1186/s40462-019-0154-8>) 
  and time domains result in specific spatiotemporal point patterns 
  and/or interactions. These emerging spatiotemporal patterns can be 
  visualized, analyzed, and then employed for both spatial and 
  temporal model assessments. Given the growing scarcity of detailed 
  spatiotemporal data, this package offers an alternative dataset 
  for a broad spectrum of studies in both the social and life sciences.
	"""
	
	homepage = "https://github.com/MAnalytics/stppSim"
	cran = "stppSim" 

	version("1.3.2", md5="35a43999ceba6010d871eb7d062159ea")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-splancs", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-ks", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-simriv", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r-sparr", type=("build", "run"))
	depends_on("r-chron", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-geosphere", type=("build", "run"))
	depends_on("r-leaflet", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-gstat", type=("build", "run"))
	depends_on("r-otusummary", type=("build", "run"))
	depends_on("r-progressr", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
