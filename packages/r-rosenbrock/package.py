# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRosenbrock(RPackage):
	"""Extended Rosenbrock-Type Densities for Markov Chain Monte Carlo
(MCMC) Sampler Benchmarking

	New Markov chain Monte Carlo (MCMC) samplers new to be thoroughly tested
    and their performance accurately assessed. This requires densities
    that offer challenging properties to the novel sampling algorithms.
    One such popular problem is the Rosenbrock function. However, while its
    shape lends itself well to a benchmark problem, no codified multivariate expansion
    of the density exists. We have developed an extension to this class of distributions
    and supplied densities and direct sampler functions to assess the performance
    of novel MCMC algorithms. The functions are introduced in "An n-dimensional Rosenbrock 
    Distribution for MCMC Testing" by Pagani, Wiegand and Nadarajah (2019) <arXiv:1903.09556>.
	"""
	
	cran = "Rosenbrock" 

	version("0.1.0", md5="9a877ee24ff0491550f2b2c6765cbcf0")

	depends_on("r-mass", type=("build", "run"))
