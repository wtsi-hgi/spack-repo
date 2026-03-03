# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCshshydrology(RPackage):
	"""Canadian Hydrological Analyses

	A collection of user-submitted functions to aid in the analysis of hydrological data, particularly for users in Canada. The functions focus on the use of Canadian data sets, and are suited to Canadian hydrology, such as the important cold region hydrological processes and will work with Canadian hydrological models. The functions are grouped into several themes, currently including Statistical hydrology, Basic data manipulations, Visualization, and Spatial hydrology. Functions developed by the Floodnet project are also included. CSHShydRology has been developed with the assistance of the Canadian Society for Hydrological Sciences (CSHS) which is an affiliated society of the Canadian Water Resources Association (CWRA). As of version 1.2.6, functions now fail gracefully when attempting to download data from a url which is unavailable.
	"""
	
	homepage = "https://github.com/CSHS-hydRology/CSHShydRology"
	cran = "CSHShydRology" 

	version("1.4.0", md5="9ae061dfa1b96481e9f8081c0cf80ea5")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-kendall", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-timedate", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggspatial", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-tidyhydat", type=("build", "run"))
	depends_on("r-whitebox", type=("build", "run"))
	depends_on("r-circular", type=("build", "run"))
	depends_on("r-openstreetmap", type=("build", "run"))
	depends_on("r-rnaturalearth", type=("build", "run"))
