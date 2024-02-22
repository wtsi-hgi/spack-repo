# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpecsverification(RPackage):
	"""Forecast Verification Routines for Ensemble Forecasts of Weather
and Climate

	A collection of forecast verification routines developed for the SPECS
    FP7 project. The emphasis is on comparative verification of ensemble forecasts of weather and climate.
	"""
	
	cran = "SpecsVerification" 

	version("0.5-3", md5="7c3349e48c6e5e1ceb0064a3e9c0cae4")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
