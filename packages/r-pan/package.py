# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPan(RPackage):
	"""Multiple imputation for multivariate panel or clustered data.

	It provides functions and examples for maximum likelihood estimation for
	generalized linear mixed models and Gibbs sampler for multivariate linear
	mixed models with incomplete data, as described in Schafer JL (1997)
	"Imputation of missing covariates under a multivariate linear mixed model".
	Technical report 97-04, Dept. of Statistics, The Pennsylvania State
	University."""

	cran = "pan"

	license("GPL-3.0-only")

	version("1.9", md5="b6c1c18a3f9b89f068878e065b1f00a4")

	depends_on("r@2.10:", type=("build", "run"))
