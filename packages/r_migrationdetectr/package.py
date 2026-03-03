# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMigrationdetectr(RPackage):
	"""Segment-Based Migration Detection Algorithm

	Detection of migration events and segments of continuous residence 
    based on irregular time series of location data
    as published in Chi et al. (2020) <doi:10.1371/journal.pone.0239408>.
	"""
	
	cran = "MigrationDetectR" 

	version("0.1.1", md5="06423184c1f97ad090303e7d516a45a8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
