# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFastts(RPackage):
	"""Fast Time Series Modeling for Seasonal Series with Exogenous
Variables

	An implementation of sparsity-ranked lasso and related methods 
    for time series data. This methodology is especially useful for 
    large time series with exogenous features and/or complex 
    seasonality. Originally described in Peterson and Cavanaugh 
    (2022) <doi:10.1007/s10182-021-00431-7> in the context of variable 
    selection with interactions and/or polynomials, ranked sparsity is 
    a philosophy with methods useful for variable selection in the 
    presence of prior informational asymmetry. This situation exists for time 
    series data with complex seasonality, as shown in Peterson and Cavanaugh 
    (2023+) <doi:10.48550/arXiv.2211.01492>, which also describes this package
    in greater detail. The sparsity-ranked penalization methods for Time Series
    implemented in 'fastTS' can fit large/complex/high-frequency time series
    quickly, even with a high-dimensional exogenous feature set. The method is
    considerably faster than its competitors, while often producing more 
    accurate predictions. Also included is a long hourly series of arrivals 
    into the University of Iowa Emergency Department with concurrent local 
    temperature.
	"""
	
	homepage = "https://petersonr.github.io/fastTS/"
	cran = "fastTS" 

	version("1.0.0", md5="845aabe2ed1dfeb1fc48aa3be197f5d8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ncvreg", type=("build", "run"))
	depends_on("r-rcpproll", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-yardstick", type=("build", "run"))
