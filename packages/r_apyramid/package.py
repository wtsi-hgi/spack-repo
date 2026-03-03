# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RApyramid(RPackage):
	"""Visualize Population Pyramids Aggregated by Age

	Provides a quick method for visualizing non-aggregated line-list
    or aggregated census data stratified by age and one or two categorical
    variables (e.g. gender and health status) with any number of values. It
    returns a 'ggplot' object, allowing the user to further customize the
    output. This package is part of the 'R4Epis' project 
    <https://r4epis.netlify.app/>.
	"""
	
	homepage = "https://github.com/R4EPI/apyramid"
	cran = "apyramid" 

	version("0.1.3", md5="e98f101ce04844f3bbf40948107dc4bb")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-ggplot2@3:", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-forcats@1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
