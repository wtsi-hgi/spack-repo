# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProjpred(RPackage):
	"""Projection Predictive Feature Selection.

	Performs projection predictive feature selection for generalized linear
	models and generalized linear and additive multilevel models (see,
	Piironen, Paasiniemi and Vehtari, 2020,
	<https://projecteuclid.org/euclid.ejs/1589335310>, Catalina, Burkner and
	Vehtari, 2020, <arXiv:2010.06994>). The package is compatible with the
	'rstanarm' and 'brms' packages, but other reference models can also be
	used. See the package vignette for more information and examples."""

	cran = "projpred"

	version("2.8.0", md5="fafea1726d0556e63e515dfc0270acfe")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-rstantools@2:", type=("build", "run"))
	depends_on("r-loo@2:", type=("build", "run"))
	depends_on("r-lme4@1.1.28:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-gamm4", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-ordinal", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-mclogit", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
