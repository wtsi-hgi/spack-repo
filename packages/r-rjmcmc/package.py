# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRjmcmc(RPackage):
	"""Reversible-Jump MCMC Using Post-Processing

	Performs reversible-jump Markov chain Monte Carlo (Green, 1995)
    <doi:10.2307/2337340>, specifically the restriction introduced by 
    Barker & Link (2013) <doi:10.1080/00031305.2013.791644>. By utilising 
    a 'universal parameter' space, RJMCMC is treated as a Gibbs sampling 
    problem. Previously-calculated posterior distributions are used to 
    quickly estimate posterior model probabilities. Jacobian matrices are 
    found using automatic differentiation. For a detailed description of
    the package, see Gelling, Schofield & Barker (2019)
    <doi:10.1111/anzs.12263>.
	"""
	
	cran = "rjmcmc" 

	version("0.4.5", md5="0b28a217372ee5799b5b3b892aee9f2c")

	depends_on("r-madness", type=("build", "run"))
	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
