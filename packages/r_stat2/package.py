# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStat2(RPackage):
	"""Interactive Document for Working with Basic Statistical Analysis

	An interactive document on  the topic of basic statistical analysis using 'rmarkdown' and 'shiny' packages. Runtime examples are provided in the package function as well as at  <https://jarvisatharva.shinyapps.io/StatisticsPrimer/>.
	"""
	
	cran = "STAT2" 

	version("0.1.0", md5="4e1c1a92f75dd97b27eec496b3aa19e7", url="https://cran.r-project.org/src/contrib/STAT2_0.1.0.tar.gz")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-psycho", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-corrgram", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-rpivottable", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
