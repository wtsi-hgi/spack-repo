# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPatientprofiles(RPackage):
	"""Identify Characteristics of Patients in the OMOP Common Data
Model

	Identify the characteristics of patients in data mapped to the Observational Medical Outcomes Partnership (OMOP) common data model.
	"""
	
	homepage = "https://darwin-eu-dev.github.io/PatientProfiles/"
	cran = "PatientProfiles" 

	version("0.7.0", md5="2133b557ac80d1a8e420962baabc275a")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-cdmconnector@1.3:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-omopgenerics@0.1.2:", type=("build", "run"))
	depends_on("r-visomopresults@0.2:", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
