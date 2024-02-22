# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpate(RPackage):
	"""Spatio-Temporal Modeling of Large Data Using a Spectral SPDE
Approach

	Functionality for spatio-temporal modeling of large data sets is provided. A Gaussian process in space and time is defined through a stochastic partial differential equation (SPDE). The SPDE is solved in the spectral space, and after discretizing in time and space, a linear Gaussian state space model is obtained. When doing inference, the main computational difficulty consists in evaluating the likelihood and in sampling from the full conditional of the spectral coefficients, or equivalently, the latent space-time process. In comparison to the traditional approach of using a spatio-temporal covariance function, the spectral SPDE approach is computationally advantageous. See Sigrist, Kuensch, and Stahel (2015) <doi:10.1111/rssb.12061> for more information on the methodology. This package aims at providing tools for two different modeling approaches. First, the SPDE based spatio-temporal model can be used as a component in a customized hierarchical Bayesian model (HBM). The functions of the package then provide parameterizations of the process part of the model as well as computationally efficient algorithms needed for doing inference with the HBM. Alternatively, the adaptive MCMC algorithm implemented in the package can be used as an algorithm for doing inference without any additional modeling. The MCMC algorithm supports data that follow a Gaussian or a censored distribution with point mass at zero. Covariates can be included in the model through a regression term.
	"""
	
	cran = "spate" 

	version("1.7.5", md5="a722f36d287ac57f3849dea660f15d2c")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-truncnorm", type=("build", "run"))
	depends_on("fftw@3.1.2:", type=("build", "link", "run"))
	depends_on("pkgconfig", type=("build", "link", "run"))
