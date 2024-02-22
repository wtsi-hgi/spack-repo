# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNutrientracker(RPackage):
	"""Food Composition Information and Dietary Assessment

	Provides a tool set for food information and dietary assessment. It 
    uses food composition data from several reference databases, including: 'USDA' (United States), 
    'CIQUAL' (France), 'BEDCA' (Spain), 'CNF' (Canada) and 'STFCJ' (Japan). 'NutrienTrackeR' calculates 
    the intake levels for both macronutrient and micronutrients, and compares them with the recommended 
    dietary allowances (RDA). It includes a number of visualization tools, such as time series 
    plots of nutrient intake, and pie-charts showing the main foods contributing to the intake 
    level of a given nutrient. A shiny app exposing the main functionalities of the package is also 
    provided.
	"""
	
	cran = "NutrienTrackeR" 

	version("1.3.0", md5="1b4ab961a87cffc2ed9a22f80296d149")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
