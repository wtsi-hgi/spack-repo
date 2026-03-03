# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPortalr(RPackage):
	"""Create Useful Summaries of the Portal Data

	Download and generate summaries for the rodent,
    plant, ant, and weather data from the Portal Project. Portal is a
    long-term (and ongoing) experimental monitoring site in the Chihuahua
    desert. The raw data files can be found at
    <https://github.com/weecology/portaldata>.
	"""
	
	homepage = "https://weecology.github.io/portalr/"
	cran = "portalr" 

	version("0.4.1", md5="1d2903d3e41c29e107b1b41ef4af8ff2")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-clipr", type=("build", "run"))
	depends_on("r-clisymbols", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-lunar", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect@1:", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
