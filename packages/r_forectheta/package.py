# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RForectheta(RPackage):
	"""Forecasting Time Series by Theta Models

	Routines for forecasting univariate time series using Theta Models.
	"""
	
	homepage = "https://www.sciencedirect.com/science/article/pii/S0169207016300243"
	cran = "forecTheta" 

	version("2.6.2", md5="b44f89c0c4702e3288de76dae6a9cf24")

	depends_on("r@2:", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-tseries", type=("build", "run"))
