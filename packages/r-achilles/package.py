# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAchilles(RPackage):
	"""Achilles Data Source Characterization

	Automated Characterization of Health Information at Large-Scale 
  Longitudinal Evidence Systems. Creates a descriptive statistics summary for 
  an Observational Medical Outcomes Partnership Common Data Model standardized 
  data source. This package includes functions for executing summary queries on 
  the specified data source and exporting reporting content for use across a 
  variety of Observational Health Data Sciences and Informatics community 
  applications. 
	"""
	
	cran = "Achilles" 

	version("1.7.2", md5="ee06db13f1a1b54c653cf67041d81915")

	depends_on("r-databaseconnector@2:", type=("build", "run"))
	depends_on("r@4:", type=("build", "run"))
	depends_on("r-sqlrender@1.6:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-parallellogger", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-tseries", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
