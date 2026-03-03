# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCommondatamodel(RPackage):
	"""OMOP CDM DDL and Documentation Generator

	Generates the scripts required to create an Observational Medical Outcomes Partnership (OMOP) Common Data Model (CDM) database and associated documentation for supported database platforms. Leverages the 'SqlRender' package to convert the Data Definition Language (DDL) script written in parameterized Structured Query Language (SQL) to the other supported dialects.
	"""
	
	cran = "CommonDataModel" 

	version("0.2.0", md5="2b3b971ad0e863e32bf44f7368de8861")

	depends_on("r-databaseconnector", type=("build", "run"))
	depends_on("r-sqlrender", type=("build", "run"))
	depends_on("r-rjava", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
