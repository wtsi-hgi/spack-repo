# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTimevarconcurrentmodel(RPackage):
	"""Concurrent Multivariate Models with Time-Varying Coefficients

	Provides a hypothesis test and variable selection algorithm for use in time-varying, concurrent regression models. The hypothesis test function is also accompanied by a plotting function which will show the estimated beta(s) and confidence band(s) from the hypothesis test. The hypothesis test function helps the user identify significant covariates within the scope of a time-varying concurrent model. The plots will show the amount of area that falls outside the confidence band(s) which is used for the test statistic within the hypothesis test. 
	"""
	
	cran = "TimeVarConcurrentModel" 

	version("1.0", md5="b879d451bd080f06a5919bcaadb7e784")

	depends_on("r-bolstad2", type=("build", "run"))
	depends_on("r-fda", type=("build", "run"))
