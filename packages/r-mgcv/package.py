# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMgcv(RPackage):
	"""Mixed GAM Computation Vehicle with Automatic Smoothness Estimation.

	Generalized additive (mixed) models, some of their extensions and  other
	generalized ridge regression with multiple smoothing  parameter estimation
	by (Restricted) Marginal Likelihood,  Generalized Cross Validation and
	similar, or using iterated  nested Laplace approximation for fully Bayesian
	inference. See  Wood (2017) <doi:10.1201/9781315370279> for an overview.
	Includes a gam() function, a wide variety of smoothers, 'JAGS'  support and
	distributions beyond the exponential family."""

	cran = "mgcv"

	license("GPL-2.0-or-later")

	version("1.9-1", md5="458c552f0fd41c12cdddbc5af6bf1fca")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-nlme@3.1.64:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
