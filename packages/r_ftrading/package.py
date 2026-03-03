# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFtrading(RPackage):
	"""Rmetrics - Trading and Rebalancing Financial Instruments

	A collection of functions for trading and rebalancing financial
	instruments. It implements various technical indicators to analyse time series such
	as moving averages or stochastic oscillators.
	"""
	
	homepage = "http://www.rmetrics.org"
	cran = "fTrading" 

	version("3042.79", md5="2063faf646712006e77de73786ded556")

	depends_on("r@2.15.1:", type=("build", "run"))
	depends_on("r-timedate", type=("build", "run"))
	depends_on("r-timeseries", type=("build", "run"))
	depends_on("r-fbasics", type=("build", "run"))
