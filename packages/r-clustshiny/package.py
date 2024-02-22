# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClustshiny(RPackage):
	"""Interactive Document for Working with Cluster Analysis

	An interactive document on  the topic of cluster analysis using 'rmarkdown' and 'shiny' packages. Runtime examples are provided in the package function as well as at  <https://analyticmodels.shinyapps.io/ClusterAnalysis/>.
	"""
	
	cran = "CLUSTShiny" 

	version("0.1.0", md5="88542379b31ae6e8a3ddfec1a5797a21")

	depends_on("r@3.0.3:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-klar", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-psycho", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
