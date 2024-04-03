# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSarima(RPackage):
	"""Simulation and Prediction with Seasonal ARIMA Models

	Functions, classes and methods for time series modelling with ARIMA
    and related models. The aim of the package is to provide consistent
    interface for the user. For example, a single function autocorrelations()
    computes various kinds of theoretical and sample autocorrelations. This is
    work in progress, see the documentation and vignettes for the current
    functionality.  Function sarima() fits extended multiplicative seasonal
    ARIMA models with trends, exogenous variables and arbitrary roots on the
    unit circle, which can be fixed or estimated (for the algebraic basis for
    this see <arXiv:2208.05055>, a paper on the methodology is being prepared).
	"""
	
	homepage = "https://geobosh.github.io/sarima/"
	cran = "sarima" 

	version("0.9.3", md5="7a98dab977d6c1e3b34017b192fb092b")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-polynomf@1.0.0:", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-lagged@0.2.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-ltsa", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
