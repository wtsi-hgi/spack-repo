# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
	
from spack.package import *
	
			
class RPfamanalyzer(RPackage):
	"""Identification of domain isotypes in pfam data

	Protein domains is one of the most import annoation of proteins we have with the Pfam database/tool being (by far) the most used tool. This R package enables the user to read the pfam prediction from both webserver and stand-alone runs into R. We have recently shown most human protein domains exist as multiple distinct variants termed domain isotypes. Different domain isotypes are used in a cell, tissue, and disease-specific manner. Accordingly, we find that domain isotypes, compared to each other, modulate, or abolish the functionality of a protein domain. This R package enables the identification and classification of such domain isotypes from Pfam data.
	"""
	
	bioc = "pfamAnalyzeR" 

	version("1.2.0", commit="de46306a062eb7112bc55eae24bccec356b44760")

	depends_on("r@4.3.0:", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
