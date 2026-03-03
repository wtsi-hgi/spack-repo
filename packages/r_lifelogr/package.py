# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLifelogr(RPackage):
	"""Life Logging

	Provides a framework for combining self-data (exercise, sleep, etc.) from multiple sources (fitbit, Apple Health), creating visualizations, and experimenting on onself.
	"""
	
	cran = "lifelogr" 

	version("0.1.0", md5="c336b8481b15409576e4778e0be26628")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-modelr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-lazyeval", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-fitbitscraper", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
