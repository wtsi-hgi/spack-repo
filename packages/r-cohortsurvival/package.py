# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCohortsurvival(RPackage):
	"""Estimate Survival from Common Data Model Cohorts

	Estimate survival using data mapped to the Observational Medical Outcomes Partnership common data model. Survival can be estimated based on user-defined study cohorts.
	"""
	
	homepage = "https://darwin-eu-dev.github.io/CohortSurvival/"
	cran = "CohortSurvival" 

	version("0.4.0", md5="ffa6f22e4ed27f46f60f5c067243c116")
	version("0.3.0", md5="c6ace5f05a3ba55613e25199bd7ba782")

	depends_on("r-cdmconnector@1.3:", type=("build", "run"))
	depends_on("r-omopgenerics", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dbplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-patientprofiles", type=("build", "run"))
	depends_on("r-visomopresults", type=("build", "run"))
	depends_on("r-rlang@0.4.11:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
