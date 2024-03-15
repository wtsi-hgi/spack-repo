# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCoin(RPackage):
	"""Conditional Inference Procedures in a Permutation Test Framework.

	Conditional inference procedures for the general independence problem
	including two-sample, K-sample (non-parametric ANOVA), correlation,
	censored, ordered and multivariate problems."""

	cran = "coin"

	license("GPL-2.0-only")

	version("1.4-3", md5="f4b32f910c2b55f75e4581c36904eed3")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-libcoin@1.0.9:", type=("build", "run"))
	depends_on("r-matrixstats@0.54:", type=("build", "run"))
	depends_on("r-modeltools@0.2.9:", type=("build", "run"))
	depends_on("r-mvtnorm@1.0.5:", type=("build", "run"))
	depends_on("r-multcomp", type=("build", "run"))
