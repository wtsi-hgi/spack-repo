# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSwmpr(RPackage):
	"""Retrieving, Organizing, and Analyzing Estuary Monitoring Data

	Tools for retrieving, organizing, and analyzing environmental
    data from the System Wide Monitoring Program of the National Estuarine
    Research Reserve System <https://cdmo.baruch.sc.edu/>. These tools
    address common challenges associated with continuous time series data
    for environmental decision making.
	"""
	
	homepage = "http://fawda123.github.io/SWMPr/"
	cran = "SWMPr" 

	version("2.5.0", md5="2174e55c996e259f62eaec4a29adc7af")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-oce", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-openair", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-suncalc", type=("build", "run"))
	depends_on("r-tictoc", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
