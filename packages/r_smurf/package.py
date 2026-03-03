# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmurf(RPackage):
	"""Sparse Multi-Type Regularized Feature Modeling

	Implementation of the SMuRF algorithm of Devriendt et al. (2021) <doi:10.1016/j.insmatheco.2020.11.010> to fit generalized linear models (GLMs) with multiple types of predictors via regularized maximum likelihood.
	"""
	
	homepage = "https://gitlab.com/TReynkens/smurf"
	cran = "smurf" 

	version("1.1.5", md5="cae1fdab01bfa542cfe6a5e9d0f5c677")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-catdata", type=("build", "run"))
	depends_on("r-glmnet@4:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.8.300.1:", type=("build", "run"))
