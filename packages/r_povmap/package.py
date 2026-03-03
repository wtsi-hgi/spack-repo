# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPovmap(RPackage):
	"""Extension to the 'emdi' Package

	The R package 'povmap' supports small area estimation of means and 
  poverty headcount rates. It adds several new features to the 'emdi' package
  (see "The R Package emdi for Estimating and Mapping Regionally Disaggregated 
  Indicators" by Kreutzmann et al. (2019) <doi:10.18637/jss.v091.i07>). 
  These include new options for incorporating survey weights, ex-post 
  benchmarking of estimates, two additional transformations, several new 
  convenient functions to assist with reporting results, and a wrapper function 
  to facilitate access from 'Stata'.
	"""
	
	homepage = "https://github.com/SSA-Statistical-Team-Projects/povmap"
	cran = "povmap" 

	version("1.0.1", md5="e36b46065e4e7a071a156e5083d55064")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-moments", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mumin", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-parallelmap", type=("build", "run"))
	depends_on("r-hlmdiag", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-readods", type=("build", "run"))
	depends_on("r-formula-tools", type=("build", "run"))
	depends_on("r-saerobust", type=("build", "run"))
	depends_on("r-spdep", type=("build", "run"))
	depends_on("r-bestnormalize", type=("build", "run"))
	depends_on("r-survey", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
