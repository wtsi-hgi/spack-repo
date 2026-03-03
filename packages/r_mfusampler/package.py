# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMfusampler(RPackage):
	"""Multivariate-from-Univariate (MfU) MCMC Sampler

	Convenience functions for multivariate MCMC using univariate samplers including:
  slice sampler with stepout and shrinkage (Neal (2003) <DOI:10.1214/aos/1056562461>),
  adaptive rejection sampler (Gilks and Wild (1992) <DOI:10.2307/2347565>),
  adaptive rejection Metropolis (Gilks et al (1995) <DOI:10.2307/2986138>), and
  univariate Metropolis with Gaussian proposal.
	"""
	
	cran = "MfUSampler" 

	version("1.1.0", md5="2d4eada03608c94eb4629e26d02098e9")

	depends_on("r-ars", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-dlm", type=("build", "run"))
