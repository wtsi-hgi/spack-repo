# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLongit(RPackage):
	"""High Dimensional Longitudinal Data Analysis Using MCMC

	High dimensional longitudinal data analysis with Markov Chain Monte Carlo(MCMC). 
             Currently support mixed effect regression with or without missing observations by considering 
             covariance structures. It provides estimates by missing at random and missing not at random assumptions.
             In this R package, we present Bayesian approaches that statisticians and clinical 
             researchers can easily use. The functions' methodology is based on the book "Bayesian Approaches in Oncology Using R and OpenBUGS" by 
             Bhattacharjee A (2020) <doi:10.1201/9780429329449-14>.
	"""
	
	cran = "longit" 

	version("0.1.0", md5="409c5fd11195e7d26581fac54899f006")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-aiccmodavg", type=("build", "run"))
	depends_on("r-missforest", type=("build", "run"))
	depends_on("r-r2jags", type=("build", "run"))
	depends_on("r-rjags", type=("build", "run"))
