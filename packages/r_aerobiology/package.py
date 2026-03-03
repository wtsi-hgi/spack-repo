# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAerobiology(RPackage):
	"""A Computational Tool for Aerobiological Data

	Different tools for managing databases of airborne particles, elaborating the main calculations and visualization of results. In a first step, data are checked using tools for quality control and all missing gaps are completed. Then, the main parameters of the pollen season are calculated and represented graphically. Multiple graphical tools are available: pollen calendars, phenological plots, time series, tendencies, interactive plots, abundance plots...
	"""
	
	cran = "AeRobiology" 

	version("2.0.1", md5="856208abfdcf26dd5434fc1b889cd1e8")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-writexl", type=("build", "run"))
	depends_on("r-ggvis", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-circular", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
