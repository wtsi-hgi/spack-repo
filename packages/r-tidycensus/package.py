# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidycensus(RPackage):
	"""Load US Census Boundary and Attribute Data as 'tidyverse' and 'sf'-Ready
	Data Frames.

	An integrated R interface to the decennial US Census and American Community
	Survey APIs and the US Census Bureau's geographic boundary files. Allows R
	users to return Census and ACS data as tidyverse-ready data frames, and
	optionally returns a list-column with feature geometry for all Census
	geographies."""

	cran = "tidycensus"

	version("1.6", md5="cffe4e33ac6e84d46d1aa9042495577b")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-tigris", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-jsonlite@1.5:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-units", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
