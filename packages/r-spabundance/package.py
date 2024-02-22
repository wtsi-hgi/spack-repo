# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpabundance(RPackage):
	"""Univariate and Multivariate Spatial Modeling of Species
Abundance

	Fits single-species (univariate) and multi-species (multivariate) non-spatial and spatial abundance models in a Bayesian framework using Markov Chain Monte Carlo (MCMC). Spatial models are fit using Nearest Neighbor Gaussian Processes (NNGPs). Details on NNGP models are given in Datta, Banerjee, Finley, and Gelfand (2016) <doi:10.1080/01621459.2015.1044091> and Finley, Datta, and Banerjee (2020) <arXiv:2001.09111>. Fits single-species and multi-species spatial and non-spatial versions of generalized linear mixed models (Gaussian, Poisson, Negative Binomial), N-mixture models (Royle 2004 <doi:10.1111/j.0006-341X.2004.00142.x>) and hierarchical distance sampling models (Royle, Dawson, Bates (2004) <doi:10.1890/03-3127>). Multi-species spatial models are fit using a spatial factor modeling approach with NNGPs for computational efficiency. 
	"""
	
	homepage = "https://www.jeffdoser.com/files/spabundance-web"
	cran = "spAbundance" 

	version("0.1.0", md5="6451c1db6b5db64602286e6672499bd0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-rann", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
