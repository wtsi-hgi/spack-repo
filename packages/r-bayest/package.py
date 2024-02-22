# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayest(RPackage):
	"""Effect Size Targeted Bayesian Two-Sample t-Tests via Markov
Chain Monte Carlo in Gaussian Mixture Models

	Provides an Markov-Chain-Monte-Carlo algorithm for Bayesian t-tests on the effect size. The underlying Gibbs sampler is based on a two-component Gaussian mixture and approximates the posterior distributions of the effect size, the difference of means and difference of standard deviations. A posterior analysis of the effect size via the region of practical equivalence is provided, too. For more details about the Gibbs sampler see Kelter (2019) <arXiv:1906.07524>.
	"""
	
	cran = "bayest" 

	version("1.4", md5="fbe6f06d44aae1d30903395d6d5472e7")

	depends_on("r-mcmcpack", type=("build", "run"))
