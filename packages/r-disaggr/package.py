# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDisaggr(RPackage):
	"""Two-Steps Benchmarks for Time Series Disaggregation

	The twoStepsBenchmark() and threeRuleSmooth() functions allow you to 
    disaggregate a low-frequency time series with higher frequency time series, 
    using the French National Accounts methodology. The aggregated sum of the 
    resulting time series is strictly equal to the low-frequency time series within the 
    benchmarking window. Typically, the low-frequency time series is an annual one, 
    unknown for the last year, and the high frequency one is either quarterly or 
    monthly. See "Methodology of quarterly national accounts", Insee Méthodes 
    N°126, by Insee (2012, ISBN:978-2-11-068613-8, <https://www.insee.fr/en/information/2579410>).
	"""
	
	homepage = "https://inseefr.github.io/disaggR/"
	cran = "disaggR" 

	version("1.0.5.2", md5="c146b515fc32c69bafe9786900886bb9")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rcolorbrewer@1.1.2:", type=("build", "run"))
