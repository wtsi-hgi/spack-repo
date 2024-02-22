# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgautomap(RPackage):
	"""Create Maps from a Column of Place Names

	Mapping tools that convert place names to coordinates on the fly.
    These 'ggplot2' extensions make maps from a data frame where one of the
    columns contains place names, without having to directly work with the
    underlying geospatial data and tools. The corresponding map data must be
    registered with 'cartographer' either by the user or by another package.
	"""
	
	homepage = "https://github.com/cidm-ph/ggautomap"
	cran = "ggautomap" 

	version("0.3.2", md5="3ad77f04fe30d81ad4f34100c4c967e1")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-cartographer@0.2:", type=("build", "run"))
	depends_on("r-cli@3.4:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-ggmapinset@0.3:", type=("build", "run"))
	depends_on("r-ggplot2@3.4.2:", type=("build", "run"))
	depends_on("r-packcircles@0.3.4:", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
	depends_on("r-sf@1:", type=("build", "run"))
	depends_on("r-tidyr@1.2:", type=("build", "run"))
	depends_on("r-vctrs@0.4:", type=("build", "run"))
