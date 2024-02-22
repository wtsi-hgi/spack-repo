# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIclick(RPackage):
	"""A Button-Based GUI for Financial and Economic Data Analysis

	A GUI designed to support the analysis of financial-economic time
    series data.
	"""
	
	cran = "iClick" 

	version("1.5", md5="9572e4d8b19e5bddd9cbc45cb493aee7")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-rugarch", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-coefplot", type=("build", "run"))
	depends_on("r-fbasics", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-openair", type=("build", "run"))
	depends_on("r-paper", type=("build", "run"))
	depends_on("r-timedate", type=("build", "run"))
	depends_on("r-timeseries", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
