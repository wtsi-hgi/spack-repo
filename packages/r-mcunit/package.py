# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMcunit(RPackage):
	"""Unit Tests for MC Methods

	Unit testing for Monte Carlo methods, particularly Markov Chain Monte Carlo (MCMC) methods, are implemented as extensions of the 'testthat' package. The MCMC methods check whether the MCMC chain has the correct invariant distribution. They do not check other properties of successful samplers such as whether the chain can reach all points, i.e. whether is recurrent. The tests require the ability to sample from the prior and to run steps of the MCMC chain. The methodology is described in Gandy and Scott (2020) <arXiv:2001.06465>.
	"""
	
	homepage = "https://bitbucket.org/agandy/mcunit/"
	cran = "mcunit" 

	version("0.3.2", md5="25b007b7c3eb08b21e93877048fd6bf1")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-testthat@2.3:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rdpack@0.7:", type=("build", "run"))
	depends_on("r-simctest@2.6:", type=("build", "run"))
