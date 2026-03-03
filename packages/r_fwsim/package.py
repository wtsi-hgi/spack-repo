# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFwsim(RPackage):
	"""Fisher-Wright Population Simulation

	Simulates a population under the Fisher-Wright model (fixed or stochastic population size) with a one-step neutral mutation process (stepwise mutation model, logistic mutation model and exponential mutation model supported). The stochastic population sizes are random Poisson distributed and different kinds of population growth are supported. For the stepwise mutation model, it is possible to specify locus and direction specific mutation rate (in terms of upwards and downwards mutation rate). Intermediate generations can be saved in order to study e.g. drift.
	"""
	
	cran = "fwsim" 

	version("0.3.4", md5="15c1f927b8d0edd4fc71cd60a2d8153c")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
