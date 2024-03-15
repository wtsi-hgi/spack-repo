# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTinytiger(RPackage):
	"""Lightweight Interface to TIGER/Line Shapefiles

	Download geographic shapes from the United States Census Bureau TIGER/Line
	Shapefiles
	<https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html>.
	Functions support downloading and reading in geographic boundary data. All
	downloads can be set up with a cache to avoid multiple downloads. Data is
	available back to 2000 for most geographies."""

	homepage = "https://alarm-redist.org/tinytiger/"
	cran = "tinytiger"

	maintainers("jgaeb")

	license("MIT")

	version("0.0.8", md5="78ef9ead68e8960e3a24a99f524900b2")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
