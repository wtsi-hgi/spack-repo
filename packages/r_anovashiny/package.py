# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnovashiny(RPackage):
	"""Interactive Document for Working with Analysis of Variance

	An interactive document on  the topic of one-way and two-way analysis of variance using 'rmarkdown' and 'shiny' packages. Runtime examples are provided in the package function as well as at  <https://kartikeyab.shinyapps.io/ANOVAShiny/>.
	"""
	
	cran = "ANOVAShiny" 

	version("0.1.0", md5="49169d01171f6d33eb54416a67738a2f")

	depends_on("r@3.0.3:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rhandsontable", type=("build", "run"))
	depends_on("r-desctools", type=("build", "run"))
	depends_on("r-hh", type=("build", "run"))
