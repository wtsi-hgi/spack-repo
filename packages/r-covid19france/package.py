# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCovid19france(RPackage):
	"""Cases of COVID-19 in France

	Imports and cleans 'opencovid19-fr'
    <https://github.com/opencovid19-fr/data> data on COVID-19 in France.
	"""
	
	cran = "covid19france" 

	version("0.1.0", md5="f464677e49dae8ec15d31e071d6366cd")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr@0.8.5:", type=("build", "run"))
	depends_on("r-glue@1.3.2:", type=("build", "run"))
	depends_on("r-lubridate@1.7.4:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-readr@1.3.1:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-tidyr@1.0.2:", type=("build", "run"))
