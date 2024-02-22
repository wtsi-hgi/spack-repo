# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTsstudio(RPackage):
	"""Functions for Time Series Analysis and Forecasting

	Provides a set of tools for descriptive and predictive analysis of time series data. That includes functions for interactive visualization of time series objects and as well utility functions for automation time series forecasting.
	"""
	
	homepage = "https://github.com/RamiKrispin/TSstudio"
	cran = "TSstudio" 

	version("0.1.7", md5="43f440389cfe771a943b10f210b623f4")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-data-table@1.11.2:", type=("build", "run"))
	depends_on("r-dplyr@0.7.5:", type=("build", "run"))
	depends_on("r-forecast@8.2:", type=("build", "run"))
	depends_on("r-forecasthybrid@2.0.10:", type=("build", "run"))
	depends_on("r-lubridate@1.6:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-plotly@4.7.1:", type=("build", "run"))
	depends_on("r-purrr@0.2.5:", type=("build", "run"))
	depends_on("r-rcolorbrewer@1.1.2:", type=("build", "run"))
	depends_on("r-reshape2@1.4.2:", type=("build", "run"))
	depends_on("r-scales@1:", type=("build", "run"))
	depends_on("r-tidyr@0.8.1:", type=("build", "run"))
	depends_on("r-tsibble@1.1.3:", type=("build", "run"))
	depends_on("r-viridis@0.5.1:", type=("build", "run"))
	depends_on("r-xts@0.12.0:", type=("build", "run"))
	depends_on("r-zoo@1.8.0:", type=("build", "run"))
