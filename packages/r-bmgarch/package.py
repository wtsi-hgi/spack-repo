# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBmgarch(RPackage):
	"""Bayesian Multivariate GARCH Models

	Fit Bayesian multivariate GARCH models using 'Stan' for full Bayesian inference. Generate (weighted) forecasts for means, variances (volatility) and correlations. Currently DCC(P,Q), CCC(P,Q), pdBEKK(P,Q), and BEKK(P,Q) parameterizations are implemented, based either on a multivariate gaussian normal or student-t distribution. DCC and CCC models are based on Engle (2002) <doi:10.1198/073500102288618487> and Bollerslev (1990). The BEKK parameterization follows Engle and Kroner (1995) <doi:10.1017/S0266466600009063> while the pdBEKK as well as the estimation approach for this package is described in Rast et al. (2020) <doi:10.31234/osf.io/j57pk>. The fitted models contain 'rstan' objects and can be examined with 'rstan' functions.  
	"""
	
	cran = "bmgarch" 

	version("2.0.0", md5="e94fb1740299dd79a19d0c7065f50d68")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rcpp@1.0.5:", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-loo", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-rstan@2.26:", type=("build", "run"))
	depends_on("r-rstantools@2.1.1:", type=("build", "run"))
	depends_on("r-bh@1.72.0.0:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.7:", type=("build", "run"))
	depends_on("r-stanheaders@2.26:", type=("build", "run"))
