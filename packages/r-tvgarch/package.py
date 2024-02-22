# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTvgarch(RPackage):
	"""Time Varying GARCH Modelling

	Simulation, estimation and inference for univariate and multivariate TV(s)-GARCH(p,q,r)-X models, where s indicates the number and shape of the transition functions, p is the ARCH order, q is the GARCH order, r is the asymmetry order, and 'X' indicates that covariates can be included. In the multivariate case, variances are estimated equation by equation and dynamic conditional correlations are allowed. The TV long-term component of the variance as in the multiplicative TV-GARCH model of Amado and Ter{"a}svirta (2013) <doi:10.1016/j.jeconom.2013.03.006> introduces non-stationarity whereas the GARCH-X short-term component describes conditional heteroscedasticity. Maximisation by parts leads to consistent and asymptotically normal estimates.
	"""
	
	homepage = "https://sites.google.com/site/susanacamposmartins"
	cran = "tvgarch" 

	version("2.4.1", md5="4dc01345f0c9503b1c5f4a183ad68420")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-garchx", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
