# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBamp(RPackage):
	"""Bayesian Age-Period-Cohort Modeling and Prediction

	Bayesian Age-Period-Cohort Modeling and Prediction using efficient Markov Chain Monte Carlo Methods. This is the R version of the previous BAMP software as described in Volker Schmid and Leonhard Held (2007) <DOI:10.18637/jss.v021.i08> Bayesian Age-Period-Cohort Modeling and Prediction - BAMP, Journal of Statistical Software 21:8. This package includes checks of convergence using Gelman's R.
	"""
	
	homepage = "https://volkerschmid.github.io/bamp/"
	cran = "bamp" 

	version("2.1.3", md5="b17245250470d0b8c611878923f49404")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
