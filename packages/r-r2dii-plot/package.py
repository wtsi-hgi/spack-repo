# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RR2diiPlot(RPackage):
	"""Visualize the Climate Scenario Alignment of a Financial
Portfolio

	Create plots to visualize the alignment of a corporate
    lending financial portfolio to climate change scenarios based on
    climate indicators (production and emission intensities) across key
    climate relevant sectors of the 'PACTA' methodology (Paris Agreement Capital 
    Transition Assessment; <https://www.transitionmonitor.com/>).
    Financial institutions use 'PACTA' to study how their capital
    allocation decisions align with climate change mitigation goals.
	"""
	
	homepage = "https://github.com/RMI-PACTA/r2dii.plot"
	cran = "r2dii.plot" 

	version("0.3.1", md5="56910c62330a2fb04c8b35c8dfae006a")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-r2dii-data", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
