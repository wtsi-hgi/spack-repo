# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPsyccleaning(RPackage):
	"""Data Cleaning for Psychological Analyses

	Useful for preparing and cleaning data. It includes functions to center data, reverse coding, dummy code and effect code data, and more.
	"""
	
	homepage = "https://jasonmoy28.github.io/psycCleaning/"
	cran = "psycCleaning" 

	version("0.1.1", md5="13df4c73b5a8df1669bc13c4db1f0885")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rlang@0.1.2:", type=("build", "run"))
