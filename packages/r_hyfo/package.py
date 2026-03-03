# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHyfo(RPackage):
	"""Hydrology and Climate Forecasting

	Focuses on data processing and visualization in hydrology and
    climate forecasting. Main function includes data extraction, data downscaling,
    data resampling, gap filler of precipitation, bias correction of forecasting
    data, flexible time series plot, and spatial map generation. It is a good pre-
    processing and post-processing tool for hydrological and hydraulic modellers.
	"""
	
	homepage = "https://yuanchao-xu.github.io/hyfo/"
	cran = "hyfo" 

	version("1.4.6", md5="1d917f90c4f9282029bcd7f1bf0c4758")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-ggplot2@1.0.1:", type=("build", "run"))
	depends_on("r-reshape2@1.4.1:", type=("build", "run"))
	depends_on("r-zoo@1.7.12:", type=("build", "run"))
	depends_on("r-sf@1.0.12:", type=("build", "run"))
	depends_on("r-plyr@1.8.3:", type=("build", "run"))
	depends_on("r-moments@0.14:", type=("build", "run"))
	depends_on("r-lmom@2.5:", type=("build", "run"))
	depends_on("r-maps@2.3.9:", type=("build", "run"))
	depends_on("r-sp@2.0.0:", type=("build", "run"))
	depends_on("r-ncdf4@1.14.1:", type=("build", "run"))
	depends_on("r-mass@7.3.39:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
