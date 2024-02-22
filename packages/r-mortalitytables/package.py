# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMortalitytables(RPackage):
	"""A Framework for Various Types of Mortality / Life Tables

	Classes to implement, analyze and plot cohort life tables
    for actuarial calculations. Birth-year dependent cohort mortality
    tables using a yearly trend to extrapolate from a base year are implemented,
    as well as period life table, cohort life tables using an age shift, and
    merged life tables. Additionally, several data sets from various countries 
    are included to provide widely-used tables out of the box.
	"""
	
	homepage = "https://gitlab.open-tools.net/R/r-mortality-tables"
	cran = "MortalityTables" 

	version("2.0.5", md5="800d4f3bd653847449bb7139cdce9917")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
