# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RR2jags(RPackage):
	"""Using R to Run 'JAGS'

	Providing wrapper functions to implement Bayesian analysis in JAGS.  Some major features include monitoring convergence of a MCMC model using Rubin and Gelman Rhat statistics, automatically running a MCMC model till it converges, and implementing parallel processing of a MCMC model for multiple chains.
	"""
	
	cran = "R2jags" 

	version("0.7-1.1", md5="ba7e6f901d8b877e389fb6b3b6fa3e45")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-rjags@3.3:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-coda@0.13:", type=("build", "run"))
	depends_on("r-r2winbugs", type=("build", "run"))
	depends_on("jags", type=("build", "link", "run"))
