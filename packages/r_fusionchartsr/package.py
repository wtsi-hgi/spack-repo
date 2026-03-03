# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFusionchartsr(RPackage):
	"""Embedding 'FusionCharts Javascript' Library in R

	FusionCharts provides awesome and minimalist functions to make beautiful interactive charts <https://www.fusioncharts.com/>.
	"""
	
	cran = "fusionchartsR" 

	version("0.0.3", md5="30bad1004f13d832f07516e6df5c10ac")

	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
