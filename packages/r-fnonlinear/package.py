# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFnonlinear(RPackage):
	"""Rmetrics - Nonlinear and Chaotic Time Series Modelling

	Provides a collection of functions for testing various aspects of
	univariate time series including independence and neglected
	nonlinearities. Further provides functions to investigate the chaotic
	behavior of time series processes and to simulate different types of chaotic
	time series maps.
	"""
	
	homepage = "https://www.rmetrics.org"
	cran = "fNonlinear" 

	version("4021.81", md5="19f60189e49ddba00e0c23b6a8113fa1")

	depends_on("r@2.15.1:", type=("build", "run"))
	depends_on("r-timedate", type=("build", "run"))
	depends_on("r-timeseries", type=("build", "run"))
	depends_on("r-fbasics", type=("build", "run"))
