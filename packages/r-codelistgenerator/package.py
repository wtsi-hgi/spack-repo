# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCodelistgenerator(RPackage):
	"""Identify Relevant Clinical Codes and Evaluate Their Use

	Generate a candidate code list for the Observational Medical Outcomes Partnership (OMOP) common data model based on string matching. For a given search strategy, a candidate code list will be returned.
	"""
	
	homepage = "https://darwin-eu.github.io/CodelistGenerator/"
	cran = "CodelistGenerator" 

	version("2.2.2", md5="0049ce3ac5d36468254a187ce51a8216")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cdmconnector@1.3:", type=("build", "run"))
	depends_on("r-checkmate@2:", type=("build", "run"))
	depends_on("r-dbi@1.1:", type=("build", "run"))
	depends_on("r-duckdb", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-magrittr@2:", type=("build", "run"))
	depends_on("r-omopgenerics@0.0.2:", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
	depends_on("r-glue@1.5:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-tidyselect@1.2:", type=("build", "run"))
	depends_on("r-tidyr@1.2:", type=("build", "run"))
	depends_on("r-cli@3.1:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-patientprofiles@0.3:", type=("build", "run"))
	depends_on("r-rjsonio", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
