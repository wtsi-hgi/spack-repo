# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REthnobotanyr(RPackage):
	"""Calculate Quantitative Ethnobotany Indices

	An implementation of the quantitative ethnobotany indices in R. The goal is to provide an easy-to-use platform for ethnobotanists to assess the cultural significance of plant species based on informant consensus. The package closely follows the paper by Tardio and Pardo-de-Santayana (2008). Tardio, J., and M. Pardo-de-Santayana, 2008. Cultural Importance Indices: A Comparative Analysis Based on the Useful Wild Plants of Southern Cantabria (Northern Spain) 1. Economic Botany, 62(1), 24-39. <doi:10.1007/s12231-007-9004-5>.
	"""
	
	homepage = "https://CRAN.R-project.org/package=ethnobotanyR"
	cran = "ethnobotanyR" 

	version("0.1.9", md5="90f3c8e273ef1b827343f7891627c72f")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggalluvial", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggridges", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
