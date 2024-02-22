# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlay(RPackage):
	"""Visualize Sports Data

	Provides functions to visualise sports data. Converts data into a 
    format suitable for plotting charts. Helps to ease the process of working with
    messy sports data to a more user friendly format. Football data is accessed 
    through 'worldfootballR' '<https://github.com/JaseZiv/worldfootballR>' which 
    gets data from 'FBref' <https://fbref.com/en>, 'Transfermarkt' <https://www.transfermarkt.com/>, 
    'Understat' <https://understat.com/>, and 'fotmob' <https://www.fotmob.com/>. 
	"""
	
	homepage = "https://joe-chelladurai.github.io/play/"
	cran = "play" 

	version("0.1.3", md5="c067449e0e49f47095ac76fd08f668b4")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-worldfootballr", type=("build", "run"))
