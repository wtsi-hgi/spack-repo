# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurvimchd(RPackage):
	"""High Dimensional Survival Data Analysis with Markov Chain Monte
Carlo

	High dimensional survival data analysis with Markov Chain Monte Carlo(MCMC). 
              Currently supports frailty data analysis. Allows for Weibull and 
              Exponential distribution. Includes function for interval censored data.
	"""
	
	cran = "SurviMChd" 

	version("0.1.2", md5="9045307d3f3fe656bac7380599649870")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rjags", type=("build", "run"))
	depends_on("r-r2jags", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
