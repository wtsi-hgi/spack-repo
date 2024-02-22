# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWinratio(RPackage):
	"""Win Ratio for Prioritized Outcomes and 95% Confidence Interval

	Calculate the win ratio for prioritized outcomes and the 95% confidence interval based on Bebu and Lachin (2016) <doi:10.1093/biostatistics/kxv032>. Three type of outcomes can be analyzed: survival "failure-time" events, repeated survival "failure-time" events and continuous or ordinal "non-failure time" events that are captured at specific time-points in the study.
	"""
	
	cran = "WinRatio" 

	version("1.0", md5="94018232e5de50ef751fe378a92b8b9f")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-tidyverse@1.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
