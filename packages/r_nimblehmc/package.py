# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNimblehmc(RPackage):
	"""Hamiltonian Monte Carlo and Other Gradient-Based MCMC Sampling
Algorithms for 'nimble'

	Provides gradient-based MCMC sampling algorithms for use with the MCMC engine provided by the 'nimble' package.  This includes two versions of Hamiltonian Monte Carlo (HMC) No-U-Turn (NUTS) sampling, and (under development) Langevin samplers.  The `NUTS_classic` sampler implements the original HMC-NUTS algorithm as described in Hoffman and Gelman (2014) <arXiv:1111.4246>.  The `NUTS` sampler is a modern version of HMC-NUTS sampling matching the HMC sampler available in version 2.32.2 of Stan (Stan Development Team, 2023). In addition, convenience functions are provided for generating and modifying MCMC configuration objects which employ HMC sampling.
	"""
	
	cran = "nimbleHMC" 

	version("0.2.1", md5="19c1f5b7a92533456365e441f287753b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-nimble@1:", type=("build", "run"))
