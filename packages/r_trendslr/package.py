# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTrendslr(RPackage):
	"""Estimating Trend, Velocity and Acceleration from Sea Level
Records

	Analysis of annual average ocean water level time series, providing
    improved estimates of trend (mean sea level) and associated real-time velocities and
    accelerations. Improved trend estimates are based on singular spectrum analysis
    methods. Various gap-filling options are included to accommodate incomplete time
    series records. The package also includes a range of diagnostic tools to inspect
    the components comprising the original time series which enables expert
    interpretation and selection of likely trend components. A wide range of
    screen and plot to file options are available in the package.
	"""
	
	cran = "TrendSLR" 

	version("1.0", md5="52e81db140aee044050cc6c24be223e3")

	depends_on("r@3.2.2:", type=("build", "run"))
	depends_on("r-changepoint@2.1.1:", type=("build", "run"))
	depends_on("r-forecast@6.2:", type=("build", "run"))
	depends_on("r-plyr@1.8.3:", type=("build", "run"))
	depends_on("r-rssa@0.13.1:", type=("build", "run"))
	depends_on("r-tseries@0.10.34:", type=("build", "run"))
	depends_on("r-zoo@1.7.12:", type=("build", "run"))
	depends_on("r-imputets@1.8:", type=("build", "run"))
