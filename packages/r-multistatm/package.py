# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultistatm(RPackage):
	"""Multivariate Statistical Methods

	Algorithms to build set partitions and commutator matrices and their use in the 
    construction of multivariate d-Hermite polynomials;  estimation and derivation of theoretical  vector moments and vector
    cumulants  of multivariate distributions; conversion formulae for multivariate moments and cumulants. Applications to
    estimation and derivation of multivariate measures of skewness and kurtosis;  estimation and derivation of asymptotic 
    covariances for d-variate Hermite polynomials, multivariate moments and cumulants and measures of skewness and kurtosis.
    The formulae implemented are discussed in Terdik (2021, ISBN:9783030813925), "Multivariate Statistical Methods".
	"""
	
	cran = "MultiStatM" 

	version("1.2.1", md5="8df9ed5769beba0a3aadceae0b691543")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-arrangements", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
