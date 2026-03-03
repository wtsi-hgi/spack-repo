# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUbms(RPackage):
	"""Bayesian Models for Data from Unmarked Animals using 'Stan'

	Fit Bayesian hierarchical models of animal abundance and occurrence
    via the 'rstan' package, the R interface to the 'Stan' C++ library.
    Supported models include single-season occupancy, dynamic occupancy, and
    N-mixture abundance models. Covariates on model parameters are specified
    using a formula-based interface similar to package 'unmarked', while also
    allowing for estimation of random slope and intercept terms. References:
    Carpenter et al. (2017) <doi:10.18637/jss.v076.i01>;
    Fiske and Chandler (2011) <doi:10.18637/jss.v043.i10>.
	"""
	
	homepage = "https://kenkellner.com/ubms/"
	cran = "ubms" 

	version("1.2.6", md5="64d180a71e829845c3456b6b17876ea8")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-unmarked", type=("build", "run"))
	depends_on("r-ggplot2@2:", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-loo", type=("build", "run"))
	depends_on("r-matrix@1.5.0:", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
	depends_on("r-rstan@2.26:", type=("build", "run"))
	depends_on("r-rstantools@2:", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.9.300.2:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-stanheaders@2.26:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.2:", type=("build", "run"))
