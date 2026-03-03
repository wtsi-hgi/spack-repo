# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFactorSwitching(RPackage):
	"""Post-Processing MCMC Outputs of Bayesian Factor Analytic Models

	A well known identifiability issue in factor analytic models is the invariance with respect to orthogonal transformations. This problem burdens the inference under a Bayesian setup, where Markov chain Monte Carlo (MCMC) methods are used to generate samples from the posterior distribution. The package applies a series of rotation, sign and permutation transformations (Papastamoulis and Ntzoufras (2022) <DOI:10.1007/s11222-022-10084-4>) into raw MCMC samples of factor loadings, which are provided by the user. The post-processed output is identifiable and can be used for MCMC inference on any parametric function of factor loadings. Comparison of multiple MCMC chains is also possible.  
	"""
	
	cran = "factor.switching" 

	version("1.4", md5="51bab4860f65443470ca24e9f7d75172")

	depends_on("r-coda", type=("build", "run"))
	depends_on("r-hdinterval", type=("build", "run"))
	depends_on("r-lpsolve", type=("build", "run"))
	depends_on("r-mcmcpack", type=("build", "run"))
