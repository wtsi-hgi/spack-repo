# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLaketemps(RPackage):
	"""Lake Temperatures Collected by Situ and Satellite Methods from
1985-2009

	Lake temperature records, metadata, and climate drivers for 291 global lakes during the time period 1985-2009. Temperature observations were collected using satellite and in situ methods. Climatic drivers and geomorphometric characteristics were also compiled and are included for each lake. Data are part of the associated publication from the Global Lake Temperature Collaboration project (http://www.laketemperature.org). See citation('laketemps') for dataset attribution.
	"""
	
	cran = "laketemps" 

	version("0.5.1", md5="c2199e5e821ffbc4312804ddd349d0d9")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
