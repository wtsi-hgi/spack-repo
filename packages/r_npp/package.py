# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNpp(RPackage):
	"""Normalized Power Prior Bayesian Analysis

	Posterior sampling in several commonly used distributions using
    normalized power prior as described in 
    Duan, Ye and Smith (2006) <doi:10.1002/env.752> and 
    Ibrahim et.al. (2015) <doi:10.1002/sim.6728>. 
    Sampling of the power parameter is achieved via 
    either independence Metropolis-Hastings or random walk Metropolis-Hastings 
    based on transformation. 
	"""
	
	cran = "NPP" 

	version("0.6.0", md5="828e3035ad49bdf6c9a002d3966aeddf")

	depends_on("r@3.5:", type=("build", "run"))
