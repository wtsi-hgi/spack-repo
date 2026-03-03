# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrism(RPackage):
	"""Access Data from the Oregon State Prism Climate Project

	Allows users to access the Oregon State Prism climate data
    (<https://prism.nacse.org/>). Using the web service API data
    can easily downloaded in bulk and loaded into R for spatial analysis.
    Some user friendly visualizations are also provided.
	"""
	
	homepage = "https://docs.ropensci.org/prism/"
	cran = "prism" 

	version("0.2.1", md5="dbfaab5788caef1a895e0a819e7e3181")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
