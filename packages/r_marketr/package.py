# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMarketr(RPackage):
	"""Tidy Calculation of Marketing Metrics Plus Quick Analysis

	Facilitates tidy calculation of popular quantitative marketing 
    metrics. It also includes functions for doing analysis that will help
    marketers and data analysts better understand the drivers and/or trends
    of these metrics. These metrics include Customer Experience Index 
    <https://go.forrester.com/analytics/cx-index/> and Net Promoter Score 
    <https://www.netpromoter.com/know/>. 
	"""
	
	cran = "marketr" 

	version("0.0.2", md5="42ce4b42855f7eebbead0475265b4f29")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr@0.8.3:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-tibble@2.1.3:", type=("build", "run"))
