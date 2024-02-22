# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExpowo(RPackage):
	"""Data Mining of Plant Diversity and Distribution for R

	Produces diversity estimates and species lists with associated global distribution for any angiosperm family and genus from 'Plants of the World Online' database <https://powo.science.kew.org/>, by interacting with the source code of each plant taxon page, and creates global maps of species richness.
	"""
	
	homepage = "https://dboslab.github.io/expowo/"
	cran = "expowo" 

	version("1.0", md5="653db1cb88e581ea23b6542a01b6269b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rnaturalearth", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
