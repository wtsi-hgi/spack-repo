# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLoo(RPackage):
	"""Efficient Leave-One-Out Cross-Validation and WAIC for BayesianModels.

	Efficient approximate leave-one-out cross-validation (LOO) for Bayesian
	models fit using Markov chain Monte Carlo, as  described in Vehtari,
	Gelman, and Gabry (2017)  <doi:10.1007/s11222-016-9696-4>.  The
	approximation uses Pareto smoothed importance sampling (PSIS),  a new
	procedure for regularizing importance weights.  As a byproduct of the
	calculations, we also obtain approximate  standard errors for estimated
	predictive errors and for the comparison  of predictive errors between
	models. The package also provides methods  for using stacking and other
	model weighting techniques to average  Bayesian predictive
	distributions."""

	cran = "loo"

	version("2.6.0", md5="fd2d6e17d9ca5069884c15467f89fad1")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-matrixstats@0.52:", type=("build", "run"))
	depends_on("pandoc@1.12.3:", type=("build", "link", "run"))
