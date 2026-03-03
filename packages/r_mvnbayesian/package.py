# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMvnbayesian(RPackage):
	"""Bayesian Analysis Framework for MVN (Mixture) Distribution

	Tools of Bayesian analysis framework using the method
  suggested by Berger (1985) <doi:10.1007/978-1-4757-4286-2> for
  multivariate normal (MVN) distribution and multivariate normal
  mixture (MixMVN) distribution:
  a) calculating Bayesian posteriori of (Mix)MVN distribution;
  b) generating random vectors of (Mix)MVN distribution;
  c) Markov chain Monte Carlo (MCMC) for (Mix)MVN distribution.
	"""
	
	homepage = "https://github.com/CubicZebra/MVNBayesian"
	cran = "MVNBayesian" 

	version("0.0.8-11", md5="3983cb8e98e0b4329e11a581e079d00e")

	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
