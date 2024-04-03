# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIncidenceprevalence(RPackage):
	"""Estimate Incidence and Prevalence using the OMOP Common Data
Model

	Calculate incidence and prevalence using data mapped to the Observational Medical Outcomes Partnership (OMOP) common data model. Incidence and prevalence can be estimated for the total population in a database or for a stratification cohort.
	"""
	
	homepage = "https://darwin-eu.github.io/IncidencePrevalence/"
	cran = "IncidencePrevalence" 

	version("0.7.2", md5="b1599597737715ecfe14d1dd4d484ed5")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-cdmconnector@1.3:", type=("build", "run"))
	depends_on("r-checkmate@2:", type=("build", "run"))
	depends_on("r-cli@3:", type=("build", "run"))
	depends_on("r-dbi@1:", type=("build", "run"))
	depends_on("r-dbplyr@2.5:", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-glue@1.5:", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-omopgenerics@0.1.2:", type=("build", "run"))
	depends_on("r-scales@1.1:", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-lubridate@1:", type=("build", "run"))
	depends_on("r-magrittr@2:", type=("build", "run"))
	depends_on("r-purrr@0.3.5:", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
	depends_on("r-stringr@1.5:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr@1.2:", type=("build", "run"))
	depends_on("r-tidyselect@1.2:", type=("build", "run"))
	depends_on("r-zip@2.2:", type=("build", "run"))
