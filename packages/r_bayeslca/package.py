# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayeslca(RPackage):
	"""Bayesian Latent Class Analysis

	Bayesian Latent Class Analysis using several different
        methods.
	"""
	
	cran = "BayesLCA" 

	version("1.9", md5="d7bc54b370583b8ebfaf9011a0838a63")

	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-mcmcpack", type=("build", "run"))
