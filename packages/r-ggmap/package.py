# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgmap(RPackage):
	"""Spatial Visualization with ggplot2.

	A collection of functions to visualize spatial data and models on top of
	static maps from various online sources (e.g Google Maps and Stamen Maps).
	It includes tools common to those tasks, including functions for
	geolocation and routing."""

	cran = "ggmap"

	version("4.0.0", md5="492b5890e6f8a3770f34f61ffdd8df48")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-ggplot2@2.2:", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-jpeg", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-bitops", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
