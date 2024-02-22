# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmodule(RPackage):
	"""Automated Markov Chain Monte Carlo for Arbitrarily Structured
Correlation Matrices

	Supports automated Markov chain Monte Carlo for arbitrarily structured correlation
    matrices. The user supplies data, a correlation matrix in symbolic form, the current state
    of the chain, a function that computes the log likelihood, and a list of prior distributions.
    The package's flagship function then carries out a parameter-at-a-time update of all correlation
    parameters, and returns the new state. The method is presented in Hughes (2023), in preparation.
	"""
	
	cran = "Rmodule" 

	version("1.0", md5="09502baf0c0e4fecbdaa7053be72842a")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
