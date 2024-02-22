# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCohorts(RPackage):
	"""Cohort Analysis Made Easy

	Functions to simplify the process of preparing event and transaction for cohort analysis.
	"""
	
	homepage = "https://github.com/PeerChristensen/cohorts"
	cran = "cohorts" 

	version("1.0.1", md5="6177525e45d09118a37fbdf52c67a365")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dtplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
