# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLcra(RPackage):
	"""Bayesian Joint Latent Class and Regression Models

	For fitting Bayesian joint latent class and regression models using
    Gibbs sampling. See the documentation for the model.
    The technical details of the model implemented here are described in Elliott,
    Michael R., Zhao, Zhangchen, Mukherjee, Bhramar, Kanaya, Alka, Needham,
    Belinda L., "Methods to account for uncertainty in latent class assignments when
    using latent classes as predictors in regression models, with application to
    acculturation strategy measures" (2020) In press at Epidemiology
    <doi:10.1097/EDE.0000000000001139>.
	"""
	
	homepage = "https://github.com/umich-biostatistics/lcra"
	cran = "lcra" 

	version("1.1.5", md5="b4bf2331c8207184d3b4435a97572dcb")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-rjags", type=("build", "run"))
	depends_on("jags@4.0.0:", type=("build", "link", "run"))
