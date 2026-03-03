# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REiaapi(RPackage):
	"""Query Data from the 'EIA' API

	Provides a function to query and extract data from the 'US Energy Information Administration' ('EIA') API V2  <https://www.eia.gov/opendata/>. The 'EIA' API provides a variety of information, in a time series format, about the energy sector in the US. The API is open, free, and requires an access key and registration at <https://www.eia.gov/opendata/>.
	"""
	
	homepage = "https://github.com/RamiKrispin/EIAapi"
	cran = "EIAapi" 

	version("0.1.2", md5="9faa9621bd66a7ca191d19c73075bdaa")

	depends_on("r-data-table@1.14.2:", type=("build", "run"))
	depends_on("r-dplyr@1.0.9:", type=("build", "run"))
	depends_on("r-jsonlite@1.8.2:", type=("build", "run"))
	depends_on("r-lubridate@1.8:", type=("build", "run"))
	depends_on("jq", type=("build", "link", "run"))
