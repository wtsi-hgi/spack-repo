# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinyloadtest(RPackage):
	"""Load Test Shiny Applications

	Assesses the number of concurrent users 'shiny'
  applications are capable of supporting, and for directing application changes
  in order to support a higher number of users. Provides facilities for recording
  'shiny' application sessions, playing recorded sessions against a target
  server at load, and analyzing the resulting metrics.
	"""
	
	homepage = "https://rstudio.github.io/shinyloadtest/"
	cran = "shinyloadtest" 

	version("1.1.0", md5="e2716449d0f1b99d010fbaa7bb70d136")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-httpuv@1.5.2:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang@0.1.2:", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-svglite", type=("build", "run"))
	depends_on("r-vroom", type=("build", "run"))
	depends_on("r-websocket@1:", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("pandoc@2.2:", type=("build", "link", "run"))
