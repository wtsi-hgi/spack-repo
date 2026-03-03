# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidyhydat(RPackage):
	"""Extract and Tidy Canadian 'Hydrometric' Data

	Provides functions to access historical and real-time national 'hydrometric'
    data from Water Survey of Canada data sources (<https://dd.weather.gc.ca/hydrometric/csv/> and
    <https://collaboration.cmc.ec.gc.ca/cmc/hydrometrics/www/>) and then applies tidy data principles.
	"""
	
	homepage = "https://docs.ropensci.org/tidyhydat/"
	cran = "tidyhydat" 

	version("0.6.1", md5="85b9d5a343eefc09ee4dd9b2b9aa5f8f")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-cli@1:", type=("build", "run"))
	depends_on("r-crayon@1.3.4:", type=("build", "run"))
	depends_on("r-dbi@0.7:", type=("build", "run"))
	depends_on("r-dbplyr@1.1:", type=("build", "run"))
	depends_on("r-dplyr@0.7.4:", type=("build", "run"))
	depends_on("r-httr@1.3.1:", type=("build", "run"))
	depends_on("r-lubridate@1.6:", type=("build", "run"))
	depends_on("r-rappdirs@0.3.1:", type=("build", "run"))
	depends_on("r-readr@1.1.1:", type=("build", "run"))
	depends_on("r-rlang@0.1.2:", type=("build", "run"))
	depends_on("r-rsqlite@2:", type=("build", "run"))
	depends_on("r-tidyr@0.7.1:", type=("build", "run"))
