# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBaystar(RPackage):
	"""On Bayesian Analysis of Threshold Autoregressive Models

	Fit two-regime threshold autoregressive (TAR) models by Markov chain Monte Carlo methods. 
	"""
	
	cran = "BAYSTAR" 

	version("0.2-10", md5="2caf6c69bff0f3807695af001cba68bb")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
