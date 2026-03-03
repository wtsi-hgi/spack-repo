# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProbshiny(RPackage):
	"""Interactive Document for Working with Basic Probability

	An interactive document on  the topic of basic probability using 'rmarkdown' and 'shiny' packages. Runtime examples are provided in the package function as well as at  <https://analyticmodels.shinyapps.io/BayesShiny/>.
	"""
	
	cran = "PROBShiny" 

	version("0.1.0", md5="276f5fd0f35c02ffac6319a82b78b858")

	depends_on("r@3.0.3:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-laplacesdemon", type=("build", "run"))
	depends_on("r-shinymatrix", type=("build", "run"))
	depends_on("r-rpivottable", type=("build", "run"))
	depends_on("r-epitools", type=("build", "run"))
