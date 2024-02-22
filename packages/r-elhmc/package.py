# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RElhmc(RPackage):
	"""Sampling from a Empirical Likelihood Bayesian Posterior of
Parameters Using Hamiltonian Monte Carlo

	A tool to draw samples from a Empirical Likelihood Bayesian posterior
   of parameters using Hamiltonian Monte Carlo.
	"""
	
	cran = "elhmc" 

	version("1.1.0", md5="1b8d1d7106a9d6d2237e4ff1de74b800")

	depends_on("r-emplik", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
