# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDataframeexplorer(RPackage):
	"""Familiarity with Dataframes Before Data Manipulation

	Real life data is muddy, fuzzy and unpredictable. This makes data manipulations tedious and bringing the data to right shape alone is a major chunk of work. Functions in this package help us get an understanding of dataframes to dramatically reduces data coding time.
	"""
	
	cran = "dataframeexplorer" 

	version("1.0.2", md5="45d5f30ca0dd1e19f30b20534b7476f2")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
