# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROpenairmaps(RPackage):
	"""Create Maps of Air Pollution Data

	Combine the air quality data analysis methods of 'openair'
    with the JavaScript 'Leaflet' (<https://leafletjs.com/>) library.
    Functionality includes plotting site maps, "directional analysis"
    figures such as polar plots, and air mass trajectories.
	"""
	
	homepage = "https://davidcarslaw.github.io/openairmaps/"
	cran = "openairmaps" 

	version("0.8.1", md5="e4b4378bfcbbc8ada248a58408f92135")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-ggmap", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggtext", type=("build", "run"))
	depends_on("r-leaflet", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-openair@2.13:", type=("build", "run"))
	depends_on("r-purrr@1:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
