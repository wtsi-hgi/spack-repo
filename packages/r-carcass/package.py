# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCarcass(RPackage):
	"""Estimation of the Number of Fatalities from Carcass Searches

	The number of bird or bat fatalities from collisions with buildings, towers or wind energy turbines can be estimated based on carcass searches and experimentally assessed carcass persistence times and searcher efficiency. Functions for estimating the probability that a bird or bat that died is found by a searcher are provided. Further functions calculate the posterior distribution of the number of fatalities based on the number of carcasses found and the estimated detection probability.
	"""
	
	cran = "carcass" 

	version("1.7", md5="4693ba66de3910093a65eccf9934d0fc")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
	depends_on("r-arm", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
