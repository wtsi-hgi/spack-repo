# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMapstats(RPackage):
	"""Geographic Display of Survey Data Statistics

	Automated calculation and visualization of survey data statistics on a color-coded (choropleth) map.
	"""
	
	cran = "mapStats" 

	version("3.1", md5="22b21e6e896e9fefb3c7399d2b3521bb")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-survey", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-classint", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-ttutils", type=("build", "run"))
