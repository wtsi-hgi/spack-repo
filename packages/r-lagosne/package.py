# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLagosne(RPackage):
	"""Interface to the Lake Multi-Scaled Geospatial and Temporal
Database

	Client for programmatic access to the Lake
    Multi-scaled Geospatial and Temporal database <https://lagoslakes.org>, with functions
    for accessing lake water quality and ecological context data for the US.
	"""
	
	homepage = "https://github.com/cont-limno/LAGOSNE"
	cran = "LAGOSNE" 

	version("2.0.3", md5="7b8c1cbe30d5cadf6fe23f0d8d8e04c7")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr@0.7:", type=("build", "run"))
	depends_on("r-rappdirs@0.3.1:", type=("build", "run"))
	depends_on("r-lazyeval@0.2:", type=("build", "run"))
	depends_on("r-purrr@0.2.2.2:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-curl@2.7:", type=("build", "run"))
	depends_on("r-stringr@1.2:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-qs", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
