# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTsdataleaks(RPackage):
	"""Exploit Data Leakages in Time Series Forecasting Competitions

	Forecasting competitions are of increasing importance as a mean to learn best practices and gain knowledge. Data leakage is one of the most common issues that can often be found in competitions. Data leaks can happen when the training data contains information about the test data. For example: randomly chosen blocks of time series are concatenated to form a new time series, scale-shifts, repeating patterns in time series,  white noise is added in the original time series to form a new time series, etc.  'tsdataleaks' package can be used to detect data leakages in a collection of  time series.
	"""
	
	homepage = "https://github.com/thiyangt/tsdataleaks"
	cran = "tsdataleaks" 

	version("2.1.1", md5="9c812c0826b0b99c9e0b1374276a6ee6")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-tibble@1.4.1:", type=("build", "run"))
	depends_on("r-ggplot2@3:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-tidyr@1.1:", type=("build", "run"))
	depends_on("r-slider", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
