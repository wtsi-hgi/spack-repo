# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesplot(RPackage):
	"""Plotting for Bayesian Models.

	Plotting functions for posterior analysis, MCMC diagnostics, prior and
	posterior predictive checks, and other visualizations to support the
	applied Bayesian workflow advocated in Gabry, Simpson, Vehtari, Betancourt,
	and Gelman (2019) <doi:10.1111/rssa.12378>. The package is designed not
	only to provide convenient functionality for users, but also a common set
	of functions that can be easily used by developers working on a variety of
	R packages for Bayesian modeling, particularly (but not exclusively)
	packages interfacing with 'Stan'."""

	cran = "bayesplot"

	license("GPL-3.0-or-later")

	version("1.11.1", md5="db04b6329bee03e730f9ee69a8132573")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-dplyr@0.8:", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-ggridges@0.5.5:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-posterior", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rlang@0.3:", type=("build", "run"))
	depends_on("r-tibble@2:", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("pandoc@1.12.3:", type=("build", "link", "run"))
