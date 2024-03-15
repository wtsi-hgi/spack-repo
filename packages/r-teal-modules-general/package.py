# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTealModulesGeneral(RPackage):
	"""General Modules for 'teal' Applications

	Prebuilt 'shiny' modules containing tools for viewing data,
    visualizing data, understanding missing and outlier values within your
    data and performing simple data analysis.  This extends 'teal'
    framework that supports reproducible research and analysis.
	"""
	
	homepage = "https://insightsengineering.github.io/teal.modules.general/"
	cran = "teal.modules.general" 

	version("0.3.0", md5="7f756deb52d3f1218b341230a56844c9")

	depends_on("r-ggmosaic@0.3:", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-shiny@1.6:", type=("build", "run"))
	depends_on("r-teal@0.15.1:", type=("build", "run"))
	depends_on("r-teal-transform@0.5:", type=("build", "run"))
	depends_on("r-checkmate@2.1:", type=("build", "run"))
	depends_on("r-dplyr@1.0.5:", type=("build", "run"))
	depends_on("r-dt@0.13:", type=("build", "run"))
	depends_on("r-forcats@1:", type=("build", "run"))
	depends_on("r-logger@0.2:", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-shinytree@0.2.8:", type=("build", "run"))
	depends_on("r-shinyvalidate", type=("build", "run"))
	depends_on("r-shinywidgets@0.5.1:", type=("build", "run"))
	depends_on("r-stringr@1.4.1:", type=("build", "run"))
	depends_on("r-teal-code@0.5:", type=("build", "run"))
	depends_on("r-teal-data@0.5:", type=("build", "run"))
	depends_on("r-teal-logger@0.1.1:", type=("build", "run"))
	depends_on("r-teal-reporter@0.3:", type=("build", "run"))
	depends_on("r-teal-widgets@0.4:", type=("build", "run"))
	depends_on("r-tern@0.9.3:", type=("build", "run"))
	depends_on("r-tibble@2:", type=("build", "run"))
	depends_on("r-tidyr@0.8.3:", type=("build", "run"))
