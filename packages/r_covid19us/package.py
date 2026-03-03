# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCovid19us(RPackage):
	"""Cases of COVID-19 in the United States

	A wrapper around the 'COVID Tracking Project API'
    <https://covidtracking.com/api/> providing data on cases of COVID-19
    in the US.
	"""
	
	cran = "covid19us" 

	version("0.1.9", md5="ce1efcb7d61a542728c6a8cfa4b522c7")

	depends_on("r-curl@4.3:", type=("build", "run"))
	depends_on("r-dplyr@0.8.3:", type=("build", "run"))
	depends_on("r-glue@1.3.1:", type=("build", "run"))
	depends_on("r-httr@1.4.1:", type=("build", "run"))
	depends_on("r-lubridate@1.7.4:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-purrr@0.3.3:", type=("build", "run"))
	depends_on("r-snakecase@0.11:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-tibble@2.1.3:", type=("build", "run"))
	depends_on("r-tidyr@1.0.2:", type=("build", "run"))
