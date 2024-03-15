# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExpowo(RPackage):
	"""Data Mining of Plant Diversity and Distribution

	Produces diversity estimates and species lists with associated global distribution for any vascular plant family and genus from 'Plants of the World Online' database <https://powo.science.kew.org/>, by interacting with the source code of each plant taxon page. It also creates global maps of species richness, graphics of species discoveries and nomenclatural changes over time.
	"""
	
	homepage = "https://dboslab.github.io/expowo/"
	cran = "expowo" 

	version("2.0", md5="c52ca0962fa202f6efa239cedf3e7e16")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rnaturalearth", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-flora", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-pupillometryr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-viridislite", type=("build", "run"))
