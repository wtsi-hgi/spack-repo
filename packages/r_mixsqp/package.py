# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMixsqp(RPackage):
	"""Sequential Quadratic Programming for Fast Maximum-Likelihood
Estimation of Mixture Proportions

	Provides an optimization method based on sequential
    quadratic programming (SQP) for maximum likelihood estimation of
    the mixture proportions in a finite mixture model where the
    component densities are known. The algorithm is expected to obtain
    solutions that are at least as accurate as the state-of-the-art
    MOSEK interior-point solver (called by function "KWDual" in the
    'REBayes' package), and they are expected to arrive at solutions
    more quickly when the number of samples is large and the number of
    mixture components is not too large. This implements the "mix-SQP"
    algorithm, with some improvements, described in Y. Kim,
    P. Carbonetto, M. Stephens & M. Anitescu (2020)
    <DOI:10.1080/10618600.2019.1689985>.
	"""
	
	homepage = "https://github.com/stephenslab/mixsqp"
	cran = "mixsqp" 

	version("0.3-54", md5="bd626e590845fdea9184479bbf181d69")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-irlba", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
