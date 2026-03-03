# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBlockmodels(RPackage):
	"""Latent and Stochastic Block Model Estimation by a 'V-EM'
Algorithm

	Latent and Stochastic Block Model estimation by a Variational EM algorithm.
             Various probability distribution are provided (Bernoulli,
             Poisson...), with or without covariates.
	"""
	
	cran = "blockmodels" 

	version("1.1.5", md5="54676c5769f1da9e25a2bf6a9112cc3e")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
