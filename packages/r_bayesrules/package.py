# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesrules(RPackage):
	"""Datasets and Supplemental Functions from Bayes Rules! Book

	Provides datasets and functions used for analysis 
  and visualizations in the Bayes Rules! book (<https://www.bayesrulesbook.com>). 
  The package contains a set of functions that summarize and plot Bayesian models from some conjugate families 
  and another set of functions for evaluation of some Bayesian models.
	"""
	
	homepage = "https://bayes-rules.github.io/bayesrules/docs/"
	cran = "bayesrules" 

	version("0.0.2", md5="20caf571a7e58511fceedd90e162ad6d")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rstanarm", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-groupdata2", type=("build", "run"))
