# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeasonalview(RPackage):
	"""Graphical User Interface for Seasonal Adjustment

	A graphical user interface to the 'seasonal' package and
  'X-13ARIMA-SEATS', the U.S. Census Bureau's seasonal adjustment software. 
  Unifies the code base of <http://www.seasonal.website> and the GUI in the
  'seasonal' package.
	"""
	
	homepage = "http://www.seasonal.website"
	cran = "seasonalview" 

	version("0.3", md5="3e50417ced3cc64be67e6cbec263ac14")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-seasonal@1.4:", type=("build", "run"))
	depends_on("r-shinydashboard@0.5.3:", type=("build", "run"))
	depends_on("r-shiny@0.14:", type=("build", "run"))
	depends_on("r-dygraphs@1.1.1.3:", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
