# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCohortexplorer(RPackage):
	"""Explorer of Profiles of Patients in a Cohort

	This software tool is designed to extract data from a randomized subset of individuals 
    within a cohort and make it available for exploration in a shiny application environment. It 
    retrieves date-stamped, event-level records from one or more data sources that represent patient 
    data in the Observational Medical Outcomes Partnership (OMOP) data model format. This tool 
    features a user-friendly interface that enables users to efficiently explore the extracted 
    profiles, thereby facilitating applications, such as reviewing structured profiles.
	"""
	
	homepage = "https://ohdsi.github.io/CohortExplorer/"
	cran = "CohortExplorer" 

	version("0.1.0", md5="d7a604d7dd4cda59859e5d19e476ec80")

	depends_on("r-databaseconnector@5:", type=("build", "run"))
	depends_on("r@4:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-parallellogger", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
