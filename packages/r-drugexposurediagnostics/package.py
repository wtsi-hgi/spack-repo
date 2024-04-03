# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDrugexposurediagnostics(RPackage):
	"""Diagnostics for OMOP Common Data Model Drug Records

	Ingredient specific diagnostics for drug exposure records in the Observational Medical Outcomes Partnership (OMOP) common data model.
	"""
	
	homepage = "https://darwin-eu.github.io/DrugExposureDiagnostics/"
	cran = "DrugExposureDiagnostics" 

	version("1.0.3", md5="9d34e28aceb2bb70faf261c158578827")
	version("1.0.4", md5="426c24b85f5002bcc4ab544a1a72058f")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-cdmconnector@1.2:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-magrittr@2:", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
	depends_on("r-tidyr@1.2:", type=("build", "run"))
	depends_on("r-tidyselect@1.2:", type=("build", "run"))
	depends_on("r-checkmate@2:", type=("build", "run"))
	depends_on("r-glue@1.5:", type=("build", "run"))
