# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REia(RPackage):
	"""API Wrapper for 'US Energy Information Administration' Open Data

	Provides API access to data from the 'US Energy Information Administration' ('EIA') <https://www.eia.gov/>.
    Use of the API requires a free API key obtainable at <https://www.eia.gov/opendata/register.php>.
    The package includes functions for searching 'EIA' data categories and importing time series and geoset time series datasets.
    Datasets returned by these functions are provided in a tidy format or alternatively in more raw form.
    It also offers helper functions for working with 'EIA' date strings and time formats and for inspecting different summaries of series metadata.
    The package also provides control over API key storage and caching of API request results.
	"""
	
	homepage = "https://docs.ropensci.org/eia/"
	cran = "eia" 

	version("0.4.1", md5="37a479ca2bf6b0f91eca65ac54daede1")

	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
