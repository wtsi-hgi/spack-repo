# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlightplot(RPackage):
	"""Plotting Flight Paths on Maps

	Provides functionality to plot airplane flight paths on maps. The plotted flight paths follow the great circle of the Earth.
	"""
	
	homepage = "https://github.com/xmc811/flightplot"
	cran = "flightplot" 

	version("0.1.0", md5="75789f9d79e08dd851d592275aaf5128")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-geosphere", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
