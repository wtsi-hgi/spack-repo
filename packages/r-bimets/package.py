# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBimets(RPackage):
	"""Time Series and Econometric Modeling

	Time series analysis, (dis)aggregation and manipulation, e.g. time series extension, merge, projection, lag, lead, delta, moving and cumulative average and product, selection by index, date and year-period, conversion to daily, monthly, quarterly, (semi)annually. Simultaneous equation models definition, estimation, simulation and forecasting with coefficient restrictions, error autocorrelation, exogenization, add-factors, impact and interim multipliers analysis, conditional equation evaluation, endogenous targeting and model renormalization, structural stability, stochastic simulation and forecast, optimal control.
	"""
	
	homepage = "https://github.com/andrea-luciani/bimets"
	cran = "bimets" 

	version("3.0.2", md5="53d2b3181e2cb783c69b3f93fab89d6b")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
