# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDrugutilisation(RPackage):
	"""Summarise Patient-Level Drug Utilisation in Data Mapped to the
OMOP Common Data Model

	Summarise patient-level drug utilisation cohorts using data mapped 
    to the Observational Medical Outcomes Partnership (OMOP) common data model. 
    New users and prevalent users cohorts can be generated and their 
    characteristics, indication and drug use summarised.
	"""
	
	homepage = "https://darwin-eu-dev.github.io/DrugUtilisation/"
	cran = "DrugUtilisation" 

	version("0.5.0", md5="7ca7bb7f10593f583cfd51d4dd2e350a")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-cdmconnector@1.3:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-dbplyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rjsonio", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-patientprofiles@0.6:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tictoc", type=("build", "run"))
	depends_on("r-omopgenerics@0.0.2:", type=("build", "run"))
	depends_on("r-visomopresults", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
