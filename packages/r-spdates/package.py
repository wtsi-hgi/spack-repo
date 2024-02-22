# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpdates(RPackage):
	"""Analysis of Spatial Gradients in Radiocarbon Dates

	Inspired by space-time regressions often performed to assess
    the expansion of the Neolithic from the Near East to Europe (Pinhasi et
    al. 2005 <doi:10.1371/journal.pbio.0030410>). Test for significant
    correlations between the (earliest) radiocarbon dates of archaeological
    sites and their respective distances from a hypothetical center of origin.
    Both ordinary least squares (OLS) and reduced major axis (RMA) methods
    are supported (Russell et al. 2014 <doi:10.1371/journal.pone.0087854>).
    It is also possible to iterate over many sites to identify the most likely
    origin.
	"""
	
	cran = "spDates" 

	version("1.1", md5="7ca86d23b0bb180ffd083b8328401d30")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcarbon", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-smatr", type=("build", "run"))
	depends_on("r-viridislite", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-gstat", type=("build", "run"))
