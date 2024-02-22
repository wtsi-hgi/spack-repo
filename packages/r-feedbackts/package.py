# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFeedbackts(RPackage):
	"""Analysis of Feedback in Time Series

	Analysis of fragmented time directionality to investigate feedback in time series. Tools provided by the package allow the analysis of feedback for a single time series and the analysis of feedback for a set of time series collected across a spatial domain.
	"""
	
	cran = "FeedbackTS" 

	version("1.5", md5="a57d8ecea9815d4ff3a3c7496a9d9a1a")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-maps", type=("build", "run"))
	depends_on("r-mapdata", type=("build", "run"))
	depends_on("r-proj4", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-gstat", type=("build", "run"))
	depends_on("r-automap", type=("build", "run"))
