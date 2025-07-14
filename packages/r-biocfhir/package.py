# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiocfhir(RPackage):
	"""Illustration of FHIR ingestion and transformation using R

	FHIR R4 bundles in JSON format are derived from https://synthea.mitre.org/downloads. Transformation inspired by a kaggle notebook published by Dr Alexander Scarlat, https://www.kaggle.com/code/drscarlat/fhir-starter-parse-healthcare-bundles-into-tables. This is a very limited illustration of some basic parsing and reorganization processes.  Additional tooling will be required to move beyond the Synthea data illustrations.
	"""
	
	homepage = "https://github.com/vjcitn/BiocFHIR"
	bioc = "BiocFHIR"

	version("1.10.0", commit="6ea9bf3625e1ed8909fe9053a6a8ad9c81d0ec95")
	version("1.4.0", commit="f169868a75ba4d8592a3be3b6b68161135a4e793")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-visnetwork", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-biocbaseutils", type=("build", "run"))
