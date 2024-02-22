# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPoisbinom(RPackage):
	"""A Faster Implementation of the Poisson-Binomial Distribution

	Provides the probability, distribution, and quantile functions and random number generator for the Poisson-Binomial distribution.  This package relies on FFTW to implement the discrete Fourier transform, so that it is much faster than the existing implementation of the same algorithm in R.
	"""
	
	cran = "poisbinom" 

	version("1.0.1", md5="fc1a1bf6eb1d9de974e817534cd80b86")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("fftw@3:", type=("build", "link", "run"))
