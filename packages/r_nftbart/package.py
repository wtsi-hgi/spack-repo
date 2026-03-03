# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNftbart(RPackage):
	"""Nonparametric Failure Time Bayesian Additive Regression Trees

	Nonparametric Failure Time (NFT) Bayesian Additive Regression Trees (BART): Time-to-event Machine Learning with Heteroskedastic Bayesian Additive Regression Trees (HBART) and Low Information Omnibus (LIO) Dirichlet Process Mixtures (DPM). An NFT BART model is of the form Y = mu + f(x) + sd(x) E where functions f and sd have BART and HBART priors, respectively, while E is a nonparametric error distribution due to a DPM LIO prior hierarchy. See the following for a complete description of the model at <doi:10.1111/biom.13857>.
	"""
	
	cran = "nftbart" 

	version("2.1", md5="15c5d632e762a3b228bbfea1adc02983")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
