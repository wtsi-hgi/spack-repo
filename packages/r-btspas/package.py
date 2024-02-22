# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBtspas(RPackage):
	"""Bayesian Time-Stratified Population Analysis

	Provides advanced Bayesian methods to estimate
	     abundance and run-timing from temporally-stratified
	     Petersen mark-recapture experiments. Methods include
	     hierarchical modelling of the capture probabilities
  	     and spline smoothing of the daily run size. Theory
  	     described in Bonner and Schwarz (2011)
         <doi:10.1111/j.1541-0420.2011.01599.x>.
	"""
	
	homepage = "https://github.com/cschwarz-stat-sfu-ca/BTSPAS"
	cran = "BTSPAS" 

	version("2021.11.2", md5="a536c14e0719aa9bb68f16f2a848e8aa")

	depends_on("r-actuar", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggforce", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-r2jags", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("jags", type=("build", "link", "run"))
