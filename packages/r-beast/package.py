# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBeast(RPackage):
	"""Bayesian Estimation of Change-Points in the Slope of
Multivariate Time-Series

	Assume that a temporal process is composed of contiguous segments with differing slopes and replicated noise-corrupted time series measurements are observed. The unknown mean of the data generating process is modelled as a piecewise linear function of time with an unknown number of change-points. The package infers the joint posterior distribution of the number and position of change-points as well as the unknown mean parameters per time-series by MCMC sampling. A-priori, the proposed model uses an overfitting number of mean parameters but, conditionally on a set of change-points, only a subset of them influences the likelihood. An exponentially decreasing prior distribution on the number of change-points gives rise to a posterior distribution concentrating on sparse representations of the underlying sequence, but also available is the Poisson distribution. See Papastamoulis et al (2017) <arXiv:1709.06111> for a detailed presentation of the method.
	"""
	
	cran = "beast" 

	version("1.1", md5="b1c154c82c59abfc0e1d566252d6a799")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
