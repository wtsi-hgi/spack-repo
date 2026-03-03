# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenest(RPackage):
	"""Generalized Mortality Estimator

	Command-line and 'shiny' GUI implementation of the GenEst models for estimating bird and bat mortality at wind and solar power facilities, following Dalthorp, et al. (2018) <doi:10.3133/tm7A2>. 
	"""
	
	cran = "GenEst" 

	version("1.4.9", md5="3c41fd7a2ea91e6ae4da70a9df6196d4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-gsl", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-hellno", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-shiny@1.4:", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
