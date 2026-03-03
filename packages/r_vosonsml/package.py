# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVosonsml(RPackage):
	"""Collecting Social Media Data and Generating Networks for
Analysis

	A suite of easy to use functions for collecting social media
    data and generating networks for analysis. Supports Twitter, YouTube,
    Reddit and web site data sources.
	"""
	
	homepage = "https://github.com/vosonlab/vosonSML"
	cran = "vosonSML" 

	version("0.32.7", md5="c8225e42328f257cc11ec9e74e9b3338")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-httr@1.3:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-textutils", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
