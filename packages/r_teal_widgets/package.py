# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTealWidgets(RPackage):
	"""'shiny' Widgets for 'teal' Applications

	Collection of 'shiny' widgets to support 'teal' applications.
    Enables the manipulation of application layout and plot or table
    settings.
	"""
	
	homepage = "https://insightsengineering.github.io/teal.widgets/"
	cran = "teal.widgets" 

	version("0.4.2", md5="ef3b01d69991822a2b025ee5a8e9d8d9")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-bslib", type=("build", "run"))
	depends_on("r-checkmate@2.1:", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-htmltools@0.5.4:", type=("build", "run"))
	depends_on("r-lifecycle@0.2:", type=("build", "run"))
	depends_on("r-rtables@0.6.6:", type=("build", "run"))
	depends_on("r-shiny@1.6:", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-shinywidgets@0.5.1:", type=("build", "run"))
	depends_on("r-styler@1.2:", type=("build", "run"))
