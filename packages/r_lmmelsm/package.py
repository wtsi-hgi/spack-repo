# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLmmelsm(RPackage):
	"""Fit Latent Multivariate Mixed Effects Location Scale Models

	In addition to modeling the expectation (location) of an outcome, mixed effects location scale models (MELSMs) include submodels on the variance components (scales) directly. This allows models on the within-group variance with mixed effects, and between-group variances with fixed effects. The MELSM can be used to model volatility, intraindividual variance, uncertainty, measurement error variance, and more. Multivariate MELSMs (MMELSMs) extend the model to include multiple correlated outcomes, and therefore multiple locations and scales. The latent multivariate MELSM (LMMELSM) further includes multiple correlated latent variables as outcomes. This package implements two-level mixed effects location scale models on multiple observed or latent outcomes, and between-group variance modeling. Williams, Martin, Liu, and Rast (2020) <doi:10.1027/1015-5759/a000624>. Hedeker, Mermelstein, and Demirtas (2008) <doi:10.1111/j.1541-0420.2007.00924.x>.
	"""
	
	cran = "LMMELSM" 

	version("0.2.0", md5="eff5637a0128786c51c142ba4ac200e1")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-formula@1.2:", type=("build", "run"))
	depends_on("r-loo@2.3:", type=("build", "run"))
	depends_on("r-mass@7:", type=("build", "run"))
	depends_on("r-nlme@3:", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
	depends_on("r-rstan@2.18.1:", type=("build", "run"))
	depends_on("r-rstantools@2.2:", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-stanheaders@2.18:", type=("build", "run"))
