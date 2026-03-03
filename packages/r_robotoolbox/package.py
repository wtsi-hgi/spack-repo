# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRobotoolbox(RPackage):
	"""Client for the 'KoboToolbox' API

	Suite of utilities for accessing and manipulating
    data from the 'KoboToolbox' API. 'KoboToolbox' is a robust
    platform designed for field data collection in various disciplines.
    This package aims to simplify the process of fetching and handling
    data from the API. Detailed documentation for the 'KoboToolbox' API
    can be found at <https://support.kobotoolbox.org/api.html>.
	"""
	
	homepage = "https://dickoa.gitlab.io/robotoolbox"
	cran = "robotoolbox" 

	version("1.3.2", md5="c48cf50af83e0778a1918cf10e09840c")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-crul@1.4:", type=("build", "run"))
	depends_on("r-rcppsimdjson@0.1.6:", type=("build", "run"))
	depends_on("r-data-table@1.14.2:", type=("build", "run"))
	depends_on("r-dplyr@1.1.2:", type=("build", "run"))
	depends_on("r-tidyr@1.3:", type=("build", "run"))
	depends_on("r-purrr@1.0.1:", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
	depends_on("r-tidyselect@1.2:", type=("build", "run"))
	depends_on("r-tibble@3.2.1:", type=("build", "run"))
	depends_on("r-stringi@1.7.6:", type=("build", "run"))
	depends_on("r-glue@1.6:", type=("build", "run"))
	depends_on("r-dm@1.0.5:", type=("build", "run"))
	depends_on("r-labelled@2.11:", type=("build", "run"))
	depends_on("r-readr@2.1:", type=("build", "run"))
	depends_on("r-cli@3.6.1:", type=("build", "run"))
