# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPoissonmultinomial(RPackage):
	"""The Poisson-Multinomial Distribution

	Implementation of the exact, normal approximation, and simulation-based methods for computing the probability mass function (pmf) and cumulative distribution function (cdf) of the Poisson-Multinomial distribution, together with a random number generator for the distribution. The exact method is based on multi-dimensional fast Fourier transformation (FFT) of the characteristic function of the Poisson-Multinomial distribution. The normal approximation method uses a multivariate normal distribution to approximate the pmf of the distribution based on central limit theorem. The simulation method is based on the law of large numbers. Details about the methods are available in Lin, Wang, and Hong (2022) <DOI:10.1007/s00180-022-01299-0>.
	"""
	
	cran = "PoissonMultinomial" 

	version("1.1", md5="51f35a0a27887816b1df1e49614283a1")

	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("fftw@3.3:", type=("build", "link", "run"))
