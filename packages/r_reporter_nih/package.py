# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReporterNih(RPackage):
	"""R Interface to the 'NIH RePORTER Project' API

	Methods to easily build requests in the non-standard JSON
    schema required by the National Institute of Health (NIH)'s 'RePORTER
    Project API' <https://api.reporter.nih.gov/#/Search/post_v2_projects_search>.
    Also retrieve and process result sets as either a ragged or flattened 'tibble'.
	"""
	
	homepage = "https://github.com/bikeactuary/repoRter.nih"
	cran = "repoRter.nih" 

	version("0.1.4", md5="b9176aca25f16160d3d2fbe04fbb58d5")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-assertthat@0.2.1:", type=("build", "run"))
	depends_on("r-crayon@1.4.1:", type=("build", "run"))
	depends_on("r-dplyr@1.0.7:", type=("build", "run"))
	depends_on("r-httr@1.4.2:", type=("build", "run"))
	depends_on("r-janitor@2.1:", type=("build", "run"))
	depends_on("r-jsonlite@1.7.2:", type=("build", "run"))
	depends_on("r-lubridate@1.7.10:", type=("build", "run"))
	depends_on("r-magrittr@2.0.1:", type=("build", "run"))
	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-tibble@3.1.3:", type=("build", "run"))
