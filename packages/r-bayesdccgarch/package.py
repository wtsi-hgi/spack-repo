# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesdccgarch(RPackage):
	"""Methods and Tools for Bayesian Dynamic Conditional Correlation
GARCH(1,1) Model

	Bayesian estimation of dynamic conditional correlation GARCH model for multivariate time series volatility (Fioruci, J.A., Ehlers, R.S. and Andrade-Filho, M.G., (2014). <doi:10.1080/02664763.2013.839635>.
	"""
	
	homepage = "https://ui.adsabs.harvard.edu/abs/2014arXiv1412.2967F/abstract"
	cran = "bayesDccGarch" 

	version("3.0.4", md5="0930bbf9d9c0ddcdfc05166e4166a6d1")

	depends_on("r@2:", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
