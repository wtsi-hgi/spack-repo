# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REdear(RPackage):
	"""Exploratory and Descriptive Event-Based Data Analysis

	Exploratory and descriptive analysis of event based data. Provides methods for describing and selecting process data, and for preparing event log data for process mining. Builds on the S3-class for event logs implemented in the package 'bupaR'.
	"""
	
	homepage = "https://bupar.net/"
	cran = "edeaR" 

	version("0.9.4", md5="f3de4d95ada55f6470ee07163d46ebc3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-bupar@0.5.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggthemes", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-miniui", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-shinytime", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
	depends_on("r-cli@3.2:", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-hms", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
