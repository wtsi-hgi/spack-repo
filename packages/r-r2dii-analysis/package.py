# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RR2diiAnalysis(RPackage):
	"""Measure Climate Scenario Alignment of Corporate Loans

	These tools help you to assess if a corporate lending
    portfolio aligns with climate goals. They summarize key climate
    indicators attributed to the portfolio (e.g. production, emission
    factors), and calculate alignment targets based on climate scenarios.
    They implement in R the last step of the free software 'PACTA' (Paris
    Agreement Capital Transition Assessment;
    <https://www.transitionmonitor.com/>). Financial institutions use 'PACTA'
    to study how their capital allocation decisions align with climate
    change mitigation goals.
	"""
	
	homepage = "https://github.com/RMI-PACTA/r2dii.analysis"
	cran = "r2dii.analysis" 

	version("0.4.0", md5="0e7c472a6290c4b910f6d22dcb59e4a9")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dplyr@0.8.5:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-r2dii-data@0.4:", type=("build", "run"))
	depends_on("r-rlang@0.1.2:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
