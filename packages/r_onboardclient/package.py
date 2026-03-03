# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROnboardclient(RPackage):
	"""Bindings for Onboard Data's Building Data API

	Provides a wrapper for the Onboard Data building data API <https://api.onboarddata.io/swagger>. Along with streamlining access to the API, this package simplifies access to sensor time series data, metadata (sensors, equipment, and buildings), and details about the Onboard data model/ontology.
	"""
	
	cran = "OnboardClient" 

	version("1.0.0", md5="c86e0e8d45a894775d25a760ad42f064")

	depends_on("r-data-table@1.14.2:", type=("build", "run"))
	depends_on("r-dplyr@1.0.10:", type=("build", "run"))
	depends_on("r-httr@1.4.4:", type=("build", "run"))
	depends_on("r-jsonlite@1.8:", type=("build", "run"))
	depends_on("r-lubridate@1.8:", type=("build", "run"))
	depends_on("r-plyr@1.8.7:", type=("build", "run"))
	depends_on("r-rrapply@1.2.5:", type=("build", "run"))
	depends_on("r-rstudioapi@0.14:", type=("build", "run"))
	depends_on("r-tibble@3.1.8:", type=("build", "run"))
	depends_on("r-tidyr@1.2.1:", type=("build", "run"))
	depends_on("r-tidyselect@1.1.2:", type=("build", "run"))
	depends_on("r-stringr@1.4.1:", type=("build", "run"))
