# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMemapp(RPackage):
	"""The Moving Epidemic Method Web Application

	The Moving Epidemic Method, created by T Vega and JE Lozano (2012, 2015) <doi:10.1111/j.1750-2659.2012.00422.x>, <doi:10.1111/irv.12330>, allows the weekly assessment of the epidemic and intensity status to help in routine respiratory infections surveillance in health systems. Allows the comparison of different epidemic indicators, timing and shape with past epidemics and across different regions or countries with different surveillance systems. Also, it gives a measure of the performance of the method in terms of sensitivity and specificity of the alert week. 'memapp' is a web application created in the Shiny framework for the 'mem' R package.
	"""
	
	homepage = "https://github.com/lozalojo/memapp"
	cran = "memapp" 

	version("2.16", md5="ef9c1995db7ffe7197cffbb80976f04c")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-shinybs", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-formattable", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-mem@2.18:", type=("build", "run"))
