# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGoogleanalyticsr(RPackage):
	"""Google Analytics API into R

	Interact with the Google Analytics 
  APIs <https://developers.google.com/analytics/>, including 
  the Core Reporting API (v3 and v4), Management API, User Activity API
  GA4's Data API and Admin API and Multi-Channel Funnel API.
	"""
	
	homepage = "https://code.markedmondson.me/googleAnalyticsR/"
	cran = "googleAnalyticsR" 

	version("1.1.0", md5="8929a47758626aeac7ab75414751895f")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-assertthat@0.2:", type=("build", "run"))
	depends_on("r-cli@2.0.2:", type=("build", "run"))
	depends_on("r-dplyr@0.8:", type=("build", "run"))
	depends_on("r-googleauthr@1.4:", type=("build", "run"))
	depends_on("r-httr@1.3.1:", type=("build", "run"))
	depends_on("r-jsonlite@1.5:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-measurementprotocol", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-purrr@0.2.2:", type=("build", "run"))
	depends_on("r-rlang@0.4.7:", type=("build", "run"))
	depends_on("r-tibble@2.0.1:", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-usethis", type=("build", "run"))
	depends_on("r-whisker", type=("build", "run"))
