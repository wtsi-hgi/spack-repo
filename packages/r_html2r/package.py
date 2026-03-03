# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHtml2r(RPackage):
	"""Convert 'HTML' to 'R' with a 'Shiny' App

	Provides a 'Shiny' app allowing to convert 'HTML' code to 'R' code (e.g. '<span>Hello</span>' to 'tags$span("Hello")'), for usage in a 'Shiny' UI.
	"""
	
	homepage = "https://github.com/stla/html2R"
	cran = "html2R" 

	version("0.1.0", md5="fbf0d497c73e474138aff2599587be67")

	depends_on("r-glue", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinyace", type=("build", "run"))
	depends_on("r-shinythemes", type=("build", "run"))
	depends_on("r-shinyjqui", type=("build", "run"))
