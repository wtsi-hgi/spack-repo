# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAllofus(RPackage):
	"""Interface for 'All of Us' Researcher Workbench

	Streamline use of the 'All of Us' Researcher Workbench (<https://www.researchallofus.org/data-tools/workbench/>)with tools to extract and manipulate data from the 'All of Us' database. Increase interoperability with the Observational Health Data Science and Informatics ('OHDSI') tool stack by decreasing reliance of 'All of Us' tools and allowing for cohort creation via 'Atlas'. Improve reproducible and transparent research using 'All of Us'.
	"""
	
	homepage = "https://roux-ohdsi.github.io/allofus/"
	cran = "allofus" 

	version("1.0.0", md5="e57e58a939e662dd06ce0984a4a757e0")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-bigrquery", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-dbplyr", type=("build", "run"))
	depends_on("r-sessioninfo", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
