# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBcea(RPackage):
	"""Bayesian Cost Effectiveness Analysis

	Produces an economic evaluation of a sample of suitable variables of
             cost and effectiveness / utility for two or more interventions,
             e.g. from a Bayesian model in the form of MCMC simulations.
             This package computes the most cost-effective alternative and
             produces graphical summaries and probabilistic sensitivity analysis,
             see Baio et al (2017) <doi:10.1007/978-3-319-55718-2>.
	"""
	
	homepage = "https://gianluca.statistica.it/software/bcea/"
	cran = "BCEA" 

	version("2.4.6", md5="3599523e7ab92a72c79e0baa9bc87638")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cli@3.3:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mcmcvis", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rstan", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
