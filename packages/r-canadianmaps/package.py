# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCanadianmaps(RPackage):
	"""Effortlessly Create Stunning Canadian Maps

	Simple and seamless access to a variety of 'StatCan' shapefiles for mapping Canadian provinces, regions, forward sortation areas, census divisions, and subdivisions using the popular 'ggplot2' package.
	"""
	
	homepage = "https://github.com/joellecayen/canadianmaps"
	cran = "canadianmaps" 

	version("1.3.0", md5="c87a9a6e4ebca99f80f1b963d4176dc7")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
