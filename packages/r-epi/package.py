# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpi(RPackage):
	"""Statistical Analysis in Epidemiology

	Functions for demographic and epidemiological analysis in
  the Lexis diagram, i.e. register and cohort follow-up data. In
  particular representation, manipulation, rate estimation and
  simulation for multistate data - the Lexis suite of functions, which
  includes interfaces to 'mstate', 'etm' and 'cmprsk' packages.
  Contains functions for Age-Period-Cohort and Lee-Carter modeling and
  a function for interval censored data and some useful functions for
  tabulation and plotting, as well as a number of epidemiological data
  sets.
	"""
	
	homepage = "http://bendixcarstensen.com/Epi/"
	cran = "Epi" 

	version("2.48", md5="d256157526f0a8ebc30daafac55fca10")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cmprsk", type=("build", "run"))
	depends_on("r-etm", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
