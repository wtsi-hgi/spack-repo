# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCbpmanager(RPackage):
	"""Generate, manage, and edit data and metadata files suitable for the import in cBioPortal for Cancer Genomics

	This R package provides an R Shiny application that enables the user to generate, manage, and edit data and metadata files suitable for the import in cBioPortal for Cancer Genomics. Create cancer studies and edit its metadata. Upload mutation data of a patient that will be concatenated to the data_mutation_extended.txt file of the study. Create and edit clinical patient data, sample data, and timeline data. Create custom timeline tracks for patients.
	"""
	
	homepage = "https://arsenij-ust.github.io/cbpManager/index.html"
	bioc = "cbpManager"

	version("1.16.0", commit="d49dd2266b1c054355b365b591ac7c3a5450a356")
	version("1.10.0", commit="2f7806e117c4cc6b644c4abcd7f94bb8e24c33b4")

	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-vroom", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-rapportools", type=("build", "run"))
	depends_on("r-basilisk", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-shinybs", type=("build", "run"))
	depends_on("r-shinycssloaders", type=("build", "run"))
	depends_on("r-rintrojs", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-markdown", type=("build", "run"))
