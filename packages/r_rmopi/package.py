# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmopi(RPackage):
	"""Risk Management and Optimization for Portfolio Investment

	Provides functions for risk management and portfolio investment of securities with practical tools for data processing and plotting. Moreover, it contains functions which perform the COS Method, an option pricing method based on the Fourier-cosine series (Fang, F. (2008) <doi:10.1137/080718061>).
	"""
	
	cran = "RMOPI" 

	version("1.1", md5="040ef2b7abc7faeacb74e77894049cda")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-timeseries", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-performanceanalytics", type=("build", "run"))
	depends_on("r-ttr", type=("build", "run"))
	depends_on("r-fportfolio", type=("build", "run"))
	depends_on("r-rugarch", type=("build", "run"))
	depends_on("r-timedate", type=("build", "run"))
