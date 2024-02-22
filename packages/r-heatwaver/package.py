# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHeatwaver(RPackage):
	"""Detect Heatwaves and Cold-Spells

	The different methods for defining, detecting, and categorising the extreme events 
    known as heatwaves or cold-spells, as first proposed in Hobday et al. (2016) <doi: 10.1016/j.pocean.2015.12.014> 
    and Hobday et al. (2018) <https://www.jstor.org/stable/26542662>. The functions in this package work on both air 
    and water temperature data. These detection algorithms may be used on non-temperature data as well.
	"""
	
	homepage = "https://robwschlegel.github.io/heatwaveR/index.html"
	cran = "heatwaveR" 

	version("0.4.6", md5="6d39427e1744b41d3da914b71ed6d20f")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-rcpp@0.12.16:", type=("build", "run"))
	depends_on("r-rcpproll", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
