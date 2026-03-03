# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCricketr(RPackage):
	"""Analyze Cricketers and Cricket Teams Based on ESPN Cricinfo
Statsguru

	Tools for analyzing performances of cricketers based on stats in
    ESPN Cricinfo Statsguru. The toolset can  be used for analysis of Tests,ODIs 
    and Twenty20 matches of both batsmen and bowlers. The package can also be used to
    analyze team performances.
	"""
	
	homepage = "https://github.com/tvganesh/cricketr"
	cran = "cricketr" 

	version("0.0.26", md5="360d44b9c8ad8baeba1bf1a7001c1d28")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scatterplot3d", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
