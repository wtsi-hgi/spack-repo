# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGofshiny(RPackage):
	"""Interactive Document for Working with Goodness of Fit Analysis

	An interactive document on  the topic of goodness of fit analysis using 'rmarkdown' and 'shiny' packages. Runtime examples are provided in the package function as well as at  <https://predanalyticssessions1.shinyapps.io/ChiSquareGOF/>.
	"""
	
	cran = "GOFShiny" 

	version("0.1.0", md5="91bc2c5ad8b5e92e460ba2ce9ed99c8e")

	depends_on("r@3.0.3:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-rhandsontable", type=("build", "run"))
