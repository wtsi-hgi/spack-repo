# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSctransform(RPackage):
	"""Variance Stabilizing Transformations for Single Cell UMI Data.

	A normalization method for single-cell UMI count data using a variance
	stabilizing transformation. The transformation is based on a negative
	binomial regression model with regularized parameters. As part of the same
	regression framework, this package also provides functions for batch
	correction, and data correction. See Hafemeister and Satija 2019
	<doi:10.1101/576827> for more details."""

	cran = "sctransform"

	license("GPL-3.0-only OR custom")

	version("0.4.1", md5="5db97bf1a8405b03140183ba9a609a65")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix@1.5.0:", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcpp@0.11:", type=("build", "run"))
