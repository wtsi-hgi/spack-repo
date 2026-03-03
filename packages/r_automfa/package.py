# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAutomfa(RPackage):
	"""Algorithms for Automatically Fitting MFA Models

	Provides methods for fitting the Mixture of Factor Analyzers (MFA) model automatically. 
    The MFA model is a mixture model where each sub-population is assumed to follow the Factor Analysis model. The Factor Analysis (FA) model is a latent variable model which assumes that observations are normally distributed, but imposes constraints on their covariance matrix. The MFA model contains two hyperparameters; g (the number of components in the mixture) and q (the number of factors in each component Factor Analysis model). Usually, the Expectation-Maximisation algorithm would be used to fit the MFA model, but this requires g and q to be known. This package treats g and q as unknowns and provides several methods which infer these values with as little input from the user as possible.
	"""
	
	cran = "autoMFA" 

	version("1.0.0", md5="928327fb8f0a5e6144e3968a10d81a51")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-usethis", type=("build", "run"))
