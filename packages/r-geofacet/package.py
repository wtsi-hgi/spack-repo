# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeofacet(RPackage):
	"""'ggplot2' Faceting Utilities for Geographical Data

	Provides geographical faceting functionality for 'ggplot2'.
    Geographical faceting arranges a sequence of plots of data for different
    geographical entities into a grid that preserves some of the geographical
    orientation.
	"""
	
	homepage = "https://github.com/hafen/geofacet"
	cran = "geofacet" 

	version("0.2.1", md5="65ec3a39794898b76e51ed38c914b0c2")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-ggplot2@3.2.1:", type=("build", "run"))
	depends_on("r-gtable", type=("build", "run"))
	depends_on("r-rnaturalearth", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-imgur", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-geogrid", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
