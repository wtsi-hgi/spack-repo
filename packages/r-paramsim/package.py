# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RParamsim(RPackage):
	"""Parameterized Simulation

	This function obtains a Random Number Generator (RNG) or collection of RNGs that replicate the required parameter(s) of a distribution for a time series of data. Consider the case of reproducing a time series data set of size 20 that uses an autoregressive (AR) model with phi = 0.8 and standard deviation equal to 1. When one checks the arima.sin() function's estimated parameters, it's possible that after a single trial or a few more, one won't find the precise parameters. This enables one to look for the ideal RNG setting for a simulation that will accurately duplicate the desired parameters.
	"""
	
	cran = "paramsim" 

	version("0.1.0", md5="ecabb56141c9244876a0e2bf41d54c8e")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
