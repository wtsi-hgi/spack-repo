# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRstrava(RPackage):
	"""Access the 'Strava' API

	Functions to access data from the 'Strava v3 API' <https://developers.strava.com/>.
	"""
	
	cran = "rStrava" 

	version("1.3.1", md5="50e943239532f882eafe5c2a7a046f8f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-geosphere", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggspatial", type=("build", "run"))
	depends_on("r-googleway", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-maptiles", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyterra", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
