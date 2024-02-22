# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesmultmeta(RPackage):
	"""Bayesian Multivariate Meta-Analysis

	Objective Bayesian inference procedures for the parameters of the
    multivariate random effects model with application to multivariate
    meta-analysis. The posterior for the model parameters, namely the overall
    mean vector and the between-study covariance matrix, are assessed by
    constructing Markov chains based on the Metropolis-Hastings algorithms as
    developed in Bodnar and Bodnar (2021) (<arXiv:2104.02105>). The
    Metropolis-Hastings algorithm is designed under the assumption of the
    normal distribution and the t-distribution when the Berger and Bernardo
    reference prior and the Jeffreys prior are assigned to the model parameters.
    Convergence properties of the generated Markov chains are investigated by
    the rank plots and the split hat-R estimate based on the rank normalization,
    which are proposed in Vehtari et al. (2021) (<DOI:10.1214/20-BA1221>).
	"""
	
	cran = "BayesMultMeta" 

	version("0.1.1", md5="316cb720f4969f8de27e690d456a2695")

	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
