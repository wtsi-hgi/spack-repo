# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCtashiny(RPackage):
	"""Interactive Application for Working with Contingency Tables

	An interactive application for working with contingency Tables. The application has a template for solving contingency table problems like chisquare test of independence,association plot between two categorical variables. Runtime examples are provided in the package function as well as at  <https://jarvisatharva.shinyapps.io/CategoricalDataAnalysis/>.
	"""
	
	cran = "CTAShiny" 

	version("0.1.0", md5="0897cb155b5604efedb17a2fe7712228")

	depends_on("r@3.0.3:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinymatrix", type=("build", "run"))
	depends_on("r-epitools", type=("build", "run"))
	depends_on("r-rpivottable", type=("build", "run"))
