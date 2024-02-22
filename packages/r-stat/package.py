# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStat(RPackage):
	"""Interactive Document for Working with Basic Statistical Analysis

	An interactive document on  the topic of basic statistical analysis using 'rmarkdown' and 'shiny' packages. Runtime examples are provided in the package function as well as at  <https://jarvisatharva.shinyapps.io/StatisticsPrimer/>.
	"""
	
	cran = "STAT" 

	version("0.1.0", md5="ab55db7f79e69f106b34af0ea9ef9024")

	depends_on("r@3.0.3:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-psycho", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-corrgram", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-rpivottable", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
