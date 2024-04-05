# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFeasts(RPackage):
	"""Feature Extraction and Statistics for Time Series

	Provides a collection of features, decomposition methods, 
    statistical summaries and graphics functions for the analysing tidy time
    series data. The package name 'feasts' is an acronym comprising of its key
    features: Feature Extraction And Statistics for Time Series.
	"""
	
	homepage = "http://feasts.tidyverts.org/"
	cran = "feasts" 

	version("0.3.2", md5="6b661b84b960def4c3eccb3269e7b995")
	version("0.3.1", md5="9b3e7251d98ba926fcf9fa334b79369e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-fabletools@0.3.1:", type=("build", "run"))
	depends_on("r-rlang@0.2:", type=("build", "run"))
	depends_on("r-tibble@1.4.1:", type=("build", "run"))
	depends_on("r-tsibble@0.9:", type=("build", "run"))
	depends_on("r-ggplot2@3:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-tidyr@0.8.3:", type=("build", "run"))
	depends_on("r-scales@1.1:", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-slider", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-gtable", type=("build", "run"))
