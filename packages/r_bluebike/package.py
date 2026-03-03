# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBluebike(RPackage):
	"""Blue Bike Comprehensive Data

	Facilitates the importation of the Boston Blue Bike trip data
    since 2015. Functions include the computation of trip distances of
    given trip data. It can also map the location of stations within a
    given radius and calculate the distance to nearby stations. Data is
    from <https://www.bluebikes.com/system-data>.
	"""
	
	cran = "bluebike" 

	version("0.0.3", md5="1fd9032c1c252a3ad42c36e28b5a6da0")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-leaflet", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
