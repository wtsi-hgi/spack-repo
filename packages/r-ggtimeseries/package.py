# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgtimeseries(RPackage):
	"""Time Series Visualisations Using the Grammar of Graphics

	Provides additional display mediums for time series visualisations.
	"""
	
	homepage = "https://github.com/thecomeonman/ggTimeSeries"
	cran = "ggTimeSeries" 

	version("1.0.2", md5="e93d006c954c853886209bd71cc93978")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
