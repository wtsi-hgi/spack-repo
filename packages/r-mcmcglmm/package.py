# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMcmcglmm(RPackage):
	"""MCMC Generalised Linear Mixed Models.

	Fits Multivariate Generalised Linear Mixed Models (and related models)
	using Markov chain Monte Carlo techniques (Hadfield 2010 J. Stat.
	Soft.)."""

	cran = "MCMCglmm"

	version("2.35", md5="5b7d995feea1beb5c2aa18f848c47b71")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-tensora", type=("build", "run"))
	depends_on("r-cubature", type=("build", "run"))
