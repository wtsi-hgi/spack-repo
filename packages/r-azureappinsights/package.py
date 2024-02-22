# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAzureappinsights(RPackage):
	"""Include Azure Application Insights in Shiny Apps

	Imports Azure Application Insights for web pages into Shiny apps
    via Microsoft's JavaScript snippet. 
    Allows app developers to submit page tracking and submit events.
	"""
	
	cran = "AzureAppInsights" 

	version("0.3.1", md5="ac5d16e5b33a9785b5957448dd00f19f")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-shiny@1.5:", type=("build", "run"))
	depends_on("r-rlang@0.4.11:", type=("build", "run"))
	depends_on("r-assertthat@0.2:", type=("build", "run"))
	depends_on("r-jsonlite@1.7.2:", type=("build", "run"))
	depends_on("r-lubridate@1.7:", type=("build", "run"))
