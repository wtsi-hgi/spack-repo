# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArsenal(RPackage):
	"""An Arsenal of 'R' Functions for Large-Scale Statistical
Summaries

	An Arsenal of 'R' functions for large-scale statistical summaries,
  which are streamlined to work within the latest reporting tools in 'R' and
  'RStudio' and which use formulas and versatile summary statistics for summary
  tables and models. The primary functions include tableby(), a Table-1-like
  summary of multiple variable types 'by' the levels of one or more categorical
  variables; paired(), a Table-1-like summary of multiple variable types paired across
  two time points; modelsum(), which performs simple model fits on one or more endpoints
  for many variables (univariate or adjusted for covariates);
  freqlist(), a powerful frequency table across many categorical variables;
  comparedf(), a function for comparing data.frames; and
  write2(), a function to output tables to a document.
	"""
	
	homepage = "https://github.com/mayoverse/arsenal"
	cran = "arsenal" 

	version("3.6.3", md5="ca74c7ac19bb20c08f1f4be39c17fb33")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-knitr@1.29:", type=("build", "run"))
