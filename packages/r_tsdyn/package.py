# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTsdyn(RPackage):
	"""Nonlinear Time Series Models with Regime Switching

	Implements nonlinear autoregressive (AR) time series models. For univariate series, a non-parametric approach is available through additive nonlinear AR. Parametric modeling and testing for regime switching dynamics is available when the transition is either direct (TAR: threshold AR) or smooth (STAR: smooth transition AR, LSTAR). For multivariate series, one can estimate a range of TVAR or threshold cointegration TVECM models with two or three regimes. Tests can be conducted for TVAR as well as for TVECM (Hansen and Seo 2002 and Seo 2006). 
	"""
	
	homepage = "https://github.com/MatthieuStigler/tsDyn/wiki"
	cran = "tsDyn" 

	version("11.0.4.1", md5="8a4de865d50eca9b374d079080d74ded")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mnormt", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-tserieschaos", type=("build", "run"))
	depends_on("r-tseries", type=("build", "run"))
	depends_on("r-vars", type=("build", "run"))
	depends_on("r-urca", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
