# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlr(RPackage):
	"""Machine Learning in R.

	Interface to a large number of classification and regression techniques,
	including machine-readable parameter descriptions. There is also an
	experimental extension for survival analysis, clustering and general,
	example-specific cost-sensitive learning. Generic resampling, including
	cross-validation, bootstrapping and subsampling.  Hyperparameter tuning
	with modern optimization techniques, for single- and multi-objective
	problems. Filter and wrapper methods for feature selection. Extension of
	basic learners with additional operations common in machine learning, also
	allowing for easy nested resampling. Most operations can be
	parallelized."""

	cran = "mlr"

	license("BSD-2-Clause")

	version("2.19.1", md5="a898da735270677538be21bec0435165")

	depends_on("r-paramhelpers@1.10:", type=("build", "run"))
	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-backports@1.1:", type=("build", "run"))
	depends_on("r-bbmisc@1.11:", type=("build", "run"))
	depends_on("r-checkmate@1.8.2:", type=("build", "run"))
	depends_on("r-data-table@1.12.4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-parallelmap@1.3:", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("gdal", type=("build", "link", "run"))
	depends_on("geos", type=("build", "link", "run"))
	depends_on("proj", type=("build", "link", "run"))
	depends_on("udunits", type=("build", "link", "run"))
	depends_on("gsl", type=("build", "link", "run"))
	depends_on("gmp", type=("build", "link", "run"))
	depends_on("glu", type=("build", "link", "run"))
	depends_on("gl", type=("build", "link", "run"))
	depends_on("jags", type=("build", "link", "run"))
	depends_on("mpfr", type=("build", "link", "run"))
	depends_on("openmpi", type=("build", "link", "run"))
