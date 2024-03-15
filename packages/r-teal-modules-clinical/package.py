# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTealModulesClinical(RPackage):
	"""'teal' Modules for Standard Clinical Outputs

	Provides user-friendly tools for creating and customizing
    clinical trial reports. By leveraging the 'teal' framework, this
    package provides 'teal' modules to easily create an interactive panel
    that allows for seamless adjustments to data presentation, thereby
    streamlining the creation of detailed and accurate reports.
	"""
	
	homepage = "https://insightsengineering.github.io/teal.modules.clinical/"
	cran = "teal.modules.clinical" 

	version("0.9.0", md5="96877ab738c13212c2016847634bbaf3")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-teal@0.15:", type=("build", "run"))
	depends_on("r-teal-transform@0.5:", type=("build", "run"))
	depends_on("r-tern@0.9.3:", type=("build", "run"))
	depends_on("r-broom@0.7.10:", type=("build", "run"))
	depends_on("r-checkmate@2.1:", type=("build", "run"))
	depends_on("r-dplyr@1.0.5:", type=("build", "run"))
	depends_on("r-dt@0.13:", type=("build", "run"))
	depends_on("r-formatters@0.5.5:", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-lifecycle@0.2:", type=("build", "run"))
	depends_on("r-logger@0.2:", type=("build", "run"))
	depends_on("r-rlistings@0.2.7:", type=("build", "run"))
	depends_on("r-rmarkdown@2.19:", type=("build", "run"))
	depends_on("r-rtables@0.6.6:", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-shiny@1.6:", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-shinyvalidate", type=("build", "run"))
	depends_on("r-shinywidgets@0.5.1:", type=("build", "run"))
	depends_on("r-teal-code@0.5:", type=("build", "run"))
	depends_on("r-teal-data@0.4:", type=("build", "run"))
	depends_on("r-teal-logger@0.1.1:", type=("build", "run"))
	depends_on("r-teal-reporter@0.2.1:", type=("build", "run"))
	depends_on("r-teal-widgets@0.4:", type=("build", "run"))
	depends_on("r-tern-gee@0.1.3:", type=("build", "run"))
	depends_on("r-tern-mmrm@0.3:", type=("build", "run"))
	depends_on("r-vistime", type=("build", "run"))
