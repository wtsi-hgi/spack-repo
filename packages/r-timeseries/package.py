# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTimeseries(RPackage):
	"""Financial Time Series Objects (Rmetrics)

	'S4' classes and various tools for financial time series:
  Basic functions such as scaling and sorting, subsetting,
  mathematical operations and statistical functions.
	"""
	
	homepage = "https://geobosh.github.io/timeSeriesDoc/"
	cran = "timeSeries" 

	version("4032.109", md5="645a2cd9432cacae6a7656b2a7c89662")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-timedate@2150.95:", type=("build", "run"))
