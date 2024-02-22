# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPmxcode(RPackage):
	"""Create Pharmacometric Models

	Provides a user interface to create or modify pharmacometric
    models for various modeling and simulation software platforms.
	"""
	
	cran = "pmxcode" 

	version("0.1.2", md5="223479e4c7352a808167fd2cc0fd6a7f")

	depends_on("r-shinybs", type=("build", "run"))
	depends_on("r-bsicons", type=("build", "run"))
	depends_on("r-bslib", type=("build", "run"))
	depends_on("r-config@0.3.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-golem@0.3.3:", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-markdown", type=("build", "run"))
	depends_on("r-pillar", type=("build", "run"))
	depends_on("r-rclipboard", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rhandsontable", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-shiny@1.7.1:", type=("build", "run"))
	depends_on("r-shinyace", type=("build", "run"))
	depends_on("r-shinyfiles", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-xfun", type=("build", "run"))
