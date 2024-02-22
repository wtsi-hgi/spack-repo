# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REkmcmc(RPackage):
	"""MCMC Procedures for Estimating Enzyme Kinetics Constants

	Functions for estimating catalytic constant and Michaelis-Menten constant
            for enzyme kinetics model using Metropolis-Hasting algorithm within Gibbs 
            sampler based on the Bayesian framework. 
	"""
	
	cran = "EKMCMC" 

	version("1.1.2", md5="409b2b49b9482c62033514ad4a5c0a78")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
