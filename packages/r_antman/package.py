# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAntman(RPackage):
	"""Anthology of Mixture Analysis Tools

	Fits finite Bayesian mixture models with a random number of components. The MCMC algorithm implemented is based on point processes as proposed by Argiento and De Iorio (2019) <arXiv:1904.09733> and offers a more computationally efficient alternative to reversible jump. Different mixture kernels can be specified: univariate Gaussian, multivariate Gaussian, univariate Poisson, and multivariate Bernoulli (latent class analysis). For the parameters characterising the mixture kernel, we specify conjugate priors, with possibly user specified hyper-parameters. We allow for different choices for the prior on the number of components: shifted Poisson, negative binomial, and point masses (i.e. mixtures with fixed number of components).
	"""
	
	homepage = "https://github.com/bbodin/AntMAN"
	cran = "AntMAN" 

	version("1.1.0", md5="f8bfd126d02b8be4d391fe9b1ecd4057")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-salso", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-mcclust", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-bayesplot", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
