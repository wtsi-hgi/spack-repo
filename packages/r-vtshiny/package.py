# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVtshiny(RPackage):
	"""Interactive Document for Working with Variance Analysis

	An interactive document on  the topic of variance analysis using 'rmarkdown' and 'shiny' packages. Runtime examples are provided in the package function as well as at  <https://predanalyticssessions1.shinyapps.io/chisquareVarianceTest/>.
	"""
	
	cran = "VTShiny" 

	version("0.1.0", md5="69b714d2120a287415ed48aeaf80748a")

	depends_on("r@3.0.3:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-envstats", type=("build", "run"))
