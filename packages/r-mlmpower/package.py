# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlmpower(RPackage):
	"""Power Analysis and Data Simulation for Multilevel Models

	
    A declarative language for specifying multilevel models,
    solving for population parameters based on specified variance-explained effect
    size measures, generating data, and conducting power analyses to determine
    sample size recommendations. The specification allows for any number of
    within-cluster effects, between-cluster effects, covariate effects
    at either level, and random coefficients. Moreover, the models do not
    assume orthogonal effects, and predictors can correlate at either level
    and accommodate models with multiple interaction effects.
	"""
	
	homepage = "https://github.com/bkeller2/mlmpower"
	cran = "mlmpower" 

	version("1.0.8", md5="9958c5c6aad13f5b413ac7a7aa680bbd")
	version("1.0.5", md5="154fbd7e0a91b3bd492acbfa9b14db29")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-lmertest", type=("build", "run"))
	depends_on("r-vartestnlme", type=("build", "run"))
