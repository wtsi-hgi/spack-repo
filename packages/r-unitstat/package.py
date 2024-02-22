# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUnitstat(RPackage):
	"""Performs Unit Root Test Statistics

	A test to understand the stability of the underlying 
    stochastic data. Helps the user’s understand whether the random variable under 
    consideration is stationary or non-stationary without any manual interpretation 
    of the results. It further ensures to check all the prerequisites and assumptions which 
    are underlying the unit root test statistics and if the underlying data is found to be non-stationary in all
    the 4 lags the function diagnoses the input data and returns with an optimised solution on the same.
	"""
	
	cran = "UnitStat" 

	version("1.1.0", md5="981c679bac1c3e56c0bc9d8445a2384e")

	depends_on("r-lmtest", type=("build", "run"))
