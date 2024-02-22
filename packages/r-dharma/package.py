# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDharma(RPackage):
	"""Residual Diagnostics for Hierarchical (Multi-Level / Mixed)
Regression Models

	The 'DHARMa' package uses a simulation-based approach to create
    readily interpretable scaled (quantile) residuals for fitted (generalized) linear mixed
    models. Currently supported are linear and generalized linear (mixed) models from 'lme4'
    (classes 'lmerMod', 'glmerMod'), 'glmmTMB' 'GLMMadaptive' and 'spaMM', generalized additive models
    ('gam' from 'mgcv'), 'glm' (including 'negbin' from 'MASS', but excluding quasi-distributions) and
    'lm' model classes. Moreover, externally created simulations, e.g. posterior predictive simulations
    from Bayesian software such as 'JAGS', 'STAN', or 'BUGS' can be processed as well.
    The resulting residuals are standardized to values between 0 and 1 and can be interpreted
    as intuitively as residuals from a linear regression. The package also provides a number of
    plot and test functions for typical model misspecification problems, such as
    over/underdispersion, zero-inflation, and residual spatial and temporal autocorrelation.
	"""
	
	homepage = "http://florianhartig.github.io/DHARMa/"
	cran = "DHARMa" 

	version("0.4.6", md5="1bc0e3ce3b7761689efc8ad828b55e5d")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-gap", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-qgam@1.3.2:", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
