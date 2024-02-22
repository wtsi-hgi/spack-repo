# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNsarfima(RPackage):
	"""Methods for Fitting and Simulating Non-Stationary ARFIMA Models

	Routines for fitting and simulating data under autoregressive fractionally integrated moving average (ARFIMA) models, without the constraint of covariance stationarity. Two fitting methods are implemented, a pseudo-maximum likelihood method and a minimum distance estimator. Mayoral, L. (2007) <doi:10.1111/j.1368-423X.2007.00202.x>. Beran, J. (1995) <doi:10.1111/j.2517-6161.1995.tb02054.x>.
	"""
	
	cran = "nsarfima" 

	version("0.2.0.0", md5="798fe22e327d8799c368b7d7917725a3")

	depends_on("r@3.6:", type=("build", "run"))
