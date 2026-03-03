# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTreatmentpatterns(RPackage):
	"""Analyzes Real-World Treatment Patterns of a Study Population of
Interest

	
    Computes treatment patterns within a given cohort using the Observational
    Medical Outcomes Partnership (OMOP) common data model (CDM). As described
    in Markus, Verhamme, Kors, and Rijnbeek (2022) <doi:10.1016/j.cmpb.2022.107081>.
	"""
	
	homepage = "https://github.com/darwin-eu-dev/TreatmentPatterns"
	cran = "TreatmentPatterns" 

	version("2.6.5", md5="b056c871907b6913e66a8ae6f319d20d")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-andromeda", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-sunburstr", type=("build", "run"))
	depends_on("r-networkd3", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
