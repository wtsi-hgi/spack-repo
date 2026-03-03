# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSankeywheel(RPackage):
	"""Create Dependency Wheels and Sankey Diagrams

	By binding R functions and the 'Highcharts' <http://www.highcharts.com/> charting library, 'sankeywheel' package provides a simple way to draw dependency wheels and sankey diagrams.
	"""
	
	homepage = "https://github.com/czxa/sankeywheel"
	cran = "sankeywheel" 

	version("0.1.0", md5="ee34dc259946db5c2d7cb029c5cd1971")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
