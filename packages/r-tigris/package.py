# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTigris(RPackage):
	"""Load Census TIGER/Line Shapefiles.

	Download TIGER/Line shapefiles from the United States Census Bureau and
	load into R as 'SpatialDataFrame' or 'sf' objects."""

	cran = "tigris"

	license("MIT")

	version("2.1", md5="c405d2689ae333c600013326bc29ab67")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-uuid", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
