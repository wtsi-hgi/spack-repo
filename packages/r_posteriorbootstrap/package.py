# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPosteriorbootstrap(RPackage):
	"""Non-Parametric Sampling with Parallel Monte Carlo

	An implementation of a non-parametric statistical model using a
    parallelised Monte Carlo sampling scheme. The method implemented in this
    package allows non-parametric inference to be regularized for small sample
    sizes, while also being more accurate than approximations such as
    variational Bayes. The concentration parameter is an effective sample size
    parameter, determining the faith we have in the model versus the data. When
    the concentration is low, the samples are close to the exact Bayesian
    logistic regression method; when the concentration is high, the samples are
    close to the simplified variational Bayes logistic regression. The method is
    described in full in the paper Lyddon, Walker, and Holmes (2018),
    "Nonparametric learning from Bayesian models with randomized objective
    functions" <arXiv:1806.11544>.
	"""
	
	homepage = "https://github.com/alan-turing-institute/PosteriorBootstrap/"
	cran = "PosteriorBootstrap" 

	version("0.1.2", md5="a1aec3b842571f0f9fdf7d0cd6d69693")

	depends_on("r-e1071@1.7.1:", type=("build", "run"))
	depends_on("r-mass@7.3.51.1:", type=("build", "run"))
