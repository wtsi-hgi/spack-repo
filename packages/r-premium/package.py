# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPremium(RPackage):
	"""Dirichlet Process Bayesian Clustering, Profile Regression

	Bayesian clustering using a Dirichlet process mixture model. This model is an alternative to regression models, non-parametrically linking a response vector to covariate data through cluster membership. The package allows Bernoulli, Binomial, Poisson, Normal, survival and categorical response, as well as Normal and discrete covariates. It also allows for fixed effects in the response model, where a spatial CAR (conditional autoregressive) term can be also included. Additionally, predictions may be made for the response, and missing values for the covariates are handled. Several samplers and label switching moves are implemented along with diagnostic tools to assess convergence. A number of R functions for post-processing of the output are also provided. In addition to fitting mixtures, it may additionally be of interest to determine which covariates actively drive the mixture components. This is implemented in the package as variable selection. The main reference for the package is Liverani, Hastie, Azizi, Papathomas and Richardson (2015) <doi:10.18637/jss.v064.i07>.
	"""
	
	homepage = "https://www.silvialiverani.com/software/"
	cran = "PReMiuM" 

	version("3.2.13", md5="3db2a33563cf6bd0c61a37fec158cea5")

	depends_on("r@3.5.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ggplot2@2.2:", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-plotrix@3.6.6:", type=("build", "run"))
	depends_on("r-gamlss-dist@4.3.1:", type=("build", "run"))
	depends_on("r-data-table@1.10.4.3:", type=("build", "run"))
	depends_on("r-spdep@0.7.7:", type=("build", "run"))
	depends_on("r-sf@1.0.8:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-bh@1.65.0.1:", type=("build", "run"))
