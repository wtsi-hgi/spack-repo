# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTestgenerator(RPackage):
	"""Integration Unit Tests for Pharmacoepidemiological Studies

	Push a sample population for unit testing on data mapped to the Observational Medical Outcomes Partnership (OMOP) Common Data Model.
	"""
	
	homepage = "https://github.com/darwin-eu-dev/TestGenerator"
	cran = "TestGenerator" 

	version("0.2.5", md5="28244d6f0d9cebb69d8360b5dd5c78ce")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-usethis", type=("build", "run"))
	depends_on("r-cdmconnector", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-duckdb", type=("build", "run"))
