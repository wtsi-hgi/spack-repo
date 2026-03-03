# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCorkscrew(RPackage):
	"""Preprocessor for Data Modeling

	Includes binning categorical variables into lesser number of categories based on t-test, converting categorical variables into continuous features 
	using the mean of the response variable for the respective categories, understanding the relationship between the response variable and predictor variables 
	using data transformations.
	"""
	
	cran = "corkscrew" 

	version("1.1", md5="a5a67f016c2cb619d483da5019240f3b")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
