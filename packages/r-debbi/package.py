# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDebbi(RPackage):
	"""Differential Evolution-Based Bayesian Inference

	Bayesian inference algorithms based on the population-based "differential evolution" (DE) algorithm. Users can obtain posterior mode (MAP) estimates via DEMAP, posterior samples via DEMCMC, and variational approximations via DEVI. 
	"""
	
	homepage = "https://github.com/bmgaldo/DEBBI"
	cran = "DEBBI" 

	version("0.1.0", md5="c11a82ad1c2723e3ff2cd0250835b6ab")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-randtoolbox", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
