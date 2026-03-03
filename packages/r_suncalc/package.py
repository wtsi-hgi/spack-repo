# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSuncalc(RPackage):
	"""Compute Sun Position, Sunlight Phases, Moon Position and Lunar
Phase

	Get sun position, sunlight phases (times for sunrise, sunset, dusk, etc.),
        moon position and lunar phase for the given location and time. Most calculations are based on the 
        formulas given in Astronomy Answers articles about position of the sun and the planets : 
        <https://www.aa.quae.nl/en/reken/zonpositie.html>.
	"""
	
	homepage = "https://github.com/datastorm-open/suncalc"
	cran = "suncalc" 

	version("0.5.1", md5="1fc9c7b1652c680c1a87fa6245e23fb3")

	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
