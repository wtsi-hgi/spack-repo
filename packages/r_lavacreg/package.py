# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLavacreg(RPackage):
	"""Latent Variable Count Regression Models

	Estimation of a multi-group count regression models (i.e., Poisson, 
    negative binomial) with latent covariates. This packages provides two extensions
    compared to ordinary count regression models based on a generalized linear model:
    First, measurement models for the predictors can be specified allowing to account 
    for measurement error. Second, the count regression can be simultaneously estimated 
    in multiple groups with stochastic group weights. The marginal maximum likelihood 
    estimation is described in Kiefer & Mayer (2020) <doi:10.1080/00273171.2020.1751027>.
	"""
	
	homepage = "https://github.com/chkiefer/lavacreg"
	cran = "lavacreg" 

	version("0.2-1", md5="04aaa6f9af66b4532947cbc44bda9a4c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-fastghquad", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-sparsegrid", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
