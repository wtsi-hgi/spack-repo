# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REnergy(RPackage):
	"""E-Statistics: Multivariate Inference via the Energy of Data.

	E-statistics (energy) tests and statistics for multivariate and univariate
	inference, including distance correlation, one-sample, two-sample, and
	multi-sample tests for comparing multivariate distributions, are
	implemented. Measuring and testing multivariate independence based on
	distance correlation, partial distance correlation, multivariate
	goodness-of-fit tests, k-groups and hierarchical clustering based on energy
	distance, testing for multivariate normality, distance components (disco)
	for non-parametric  analysis of structured data, and other energy
	statistics/methods are implemented."""

	cran = "energy"

	version("1.7-11", md5="d27d7739a60071b84913abf71cd0a7b2")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-gsl", type=("build", "run"))
