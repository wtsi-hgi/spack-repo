# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmarineheatwaves(RPackage):
	"""Detect Marine Heat Waves and Marine Cold Spells

	Given a time series of daily temperatures, the package provides tools
    to detect extreme thermal events, including marine heat waves, and to
    calculate the exceedances above or below specified threshold values.
    It outputs the properties of all detected events and exceedances.
	"""
	
	homepage = "https://github.com/ajsmit/RmarineHeatWaves"
	cran = "RmarineHeatWaves" 

	version("0.17.0", md5="c72444e70242f758a7c8674b85927851")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-lazyeval", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
