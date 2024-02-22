# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQuantreg(RPackage):
	"""Quantile Regression.

	Estimation and inference methods for models of conditional quantiles:
	Linear and nonlinear parametric and non-parametric (total variation
	penalized) models  for conditional quantiles of a univariate response and
	several methods for handling censored survival data.  Portfolio selection
	methods based on expected shortfall risk are also now included. See Koenker
	(2006) <doi:10.1017/CBO9780511754098> and Koenker et al. (2017)
	<doi:10.1201/9781315120256>."""

	cran = "quantreg"

	version("5.97", md5="e36187123dc53900e967b3c466a902fc")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-sparsem", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-matrixmodels", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
