# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RApexcharter(RPackage):
	"""Create Interactive Chart with the JavaScript 'ApexCharts'
Library

	Provides an 'htmlwidgets' interface to 'apexcharts.js'. 
  'Apexcharts' is a modern JavaScript charting library to build interactive charts and visualizations with simple API.
  'Apexcharts' examples and documentation are available here: <https://apexcharts.com/>.
	"""
	
	homepage = "https://github.com/dreamRs/apexcharter"
	cran = "apexcharter" 

	version("0.4.2", md5="30b25e86787bebe6ecf52fe50f6cdb54")
	version("0.4.1", md5="db5614a0052d4a4bc2491ee14b7cb3ab")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-htmlwidgets@1.5.3:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-shiny@1.1:", type=("build", "run"))
