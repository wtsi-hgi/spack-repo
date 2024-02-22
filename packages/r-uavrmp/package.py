# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUavrmp(RPackage):
	"""UAV Mission Planner

	The Unmanned Aerial Vehicle Mission Planner provides an easy to use work flow for planning autonomous obstacle avoiding surveys of (almost) ready to fly unmanned aerial vehicles to retrieve aerial or spot related data. It creates either intermediate flight control files for the DJI-Litchi supported series or ready to upload control files for the pixhawk-based flight controller as used in the 3DR-Solo. Additionally it contains some useful tools for digitizing and data manipulation.
	"""
	
	homepage = "https://github.com/gisma/uavRmp"
	cran = "uavRmp" 

	version("0.6.2", md5="9685edd0c0e176d95fd8080e0f346c81")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-geosphere", type=("build", "run"))
	depends_on("r-log4r", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-brew", type=("build", "run"))
	depends_on("r-exifr", type=("build", "run"))
	depends_on("r-link2gi", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-rlist", type=("build", "run"))
