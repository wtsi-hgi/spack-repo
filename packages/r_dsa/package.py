# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDsa(RPackage):
	"""Seasonal Adjustment of Daily Time Series

	Seasonal- and calendar adjustment of time series
    with daily frequency using the DSA approach developed by Ollech,
    Daniel (2018): Seasonal adjustment of daily time series. Bundesbank
    Discussion Paper 41/2018.
	"""
	
	cran = "dsa" 

	version("1.0.12", md5="dea8ea2b2fc9f5c4303306422074393e")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-r2html", type=("build", "run"))
	depends_on("r-tsoutliers", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-rjava", type=("build", "run"))
	depends_on("r-timedate", type=("build", "run"))
	depends_on("r-dygraphs", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-seastests", type=("build", "run"))
