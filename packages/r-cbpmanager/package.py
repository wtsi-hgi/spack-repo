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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/cbpManager_1.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/cbpManager/cbpManager_1.10.0.tar.gz"]

    version("1.16.0", tag="RELEASE_3_21")
	version("1.10.0", sha256="eae8cba70f474680fc076773ed7bc142512824c9997a326e185ce3ecb17aa784")

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
