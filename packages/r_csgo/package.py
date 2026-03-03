# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCsgo(RPackage):
	"""Collecting Counter Strike Global Offensive Data

	An implementation of calls designed to collect and organize in an easy way the data from the Steam API specifically for the Counter-Strike Global Offensive Game (CS Go) <https://developer.valvesoftware.com/wiki/Steam_Web_API>.
	"""
	
	homepage = "https://github.com/adsoncostanzifilho/CSGo"
	cran = "CSGo" 

	version("0.6.7", md5="c45cf64d7dabf056a6fa00df062a7c95")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-fuzzyjoin", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-extrafont", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
