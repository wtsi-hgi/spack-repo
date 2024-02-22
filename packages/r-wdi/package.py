# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWdi(RPackage):
	"""World Development Indicators and Other World Bank Data

	Search and download data from over 40 databases hosted by the World Bank, including the World Development Indicators ('WDI'), International Debt Statistics, Doing Business, Human Capital Index, and Sub-national Poverty indicators.
	"""
	
	homepage = "https://vincentarelbundock.github.io/WDI/"
	cran = "WDI" 

	version("2.7.8", md5="3e8fd8568bf9629c21c2428b029e661d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
