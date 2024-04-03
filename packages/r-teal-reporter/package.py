# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTealReporter(RPackage):
	"""Reporting Tools for 'shiny' Modules

	Prebuilt 'shiny' modules containing tools for the generation
    of 'rmarkdown' reports, supporting reproducible research and analysis.
	"""
	
	homepage = "https://github.com/insightsengineering/teal.reporter"
	cran = "teal.reporter" 

	version("0.3.1", md5="6b88309ac1bf98f83e83262fa8045239")

	depends_on("r-bslib", type=("build", "run"))
	depends_on("r-checkmate@2.1:", type=("build", "run"))
	depends_on("r-flextable@0.9.2:", type=("build", "run"))
	depends_on("r-htmltools@0.5.4:", type=("build", "run"))
	depends_on("r-knitr@1.34:", type=("build", "run"))
	depends_on("r-lifecycle@0.2:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rmarkdown@2.19:", type=("build", "run"))
	depends_on("r-shiny@1.6:", type=("build", "run"))
	depends_on("r-shinybusy", type=("build", "run"))
	depends_on("r-shinywidgets@0.5.1:", type=("build", "run"))
	depends_on("r-yaml@1.1:", type=("build", "run"))
	depends_on("r-zip@1.1:", type=("build", "run"))
