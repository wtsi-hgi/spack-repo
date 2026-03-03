# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsltrend(RPackage):
	"""Improved Techniques to Estimate Trend, Velocity and Acceleration
from Sea Level Records

	Analysis of annual average ocean water level time series
    from long (minimum length 80 years) individual records, providing improved
    estimates of trend (mean sea level) and associated real-time velocities and
    accelerations. Improved trend estimates are based on Singular Spectrum Analysis
    methods. Various gap-filling options are included to accommodate incomplete time
    series records. The package also contains a forecasting module to consider the
    implication of user defined quantum of sea level rise between the end of the
    available historical record and the year 2100. A wide range of screen and pdf
    plotting options are available in the package.
	"""
	
	cran = "msltrend" 

	version("1.0", md5="ffb7ed0398c5aa0a37a101ae23230c00")

	depends_on("r@3.2.2:", type=("build", "run"))
	depends_on("r-changepoint@2.1.1:", type=("build", "run"))
	depends_on("r-forecast@6.2:", type=("build", "run"))
	depends_on("r-plyr@1.8.3:", type=("build", "run"))
	depends_on("r-rssa@0.13.1:", type=("build", "run"))
	depends_on("r-tseries@0.10.34:", type=("build", "run"))
	depends_on("r-zoo@1.7.12:", type=("build", "run"))
