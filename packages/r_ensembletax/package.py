# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REnsembletax(RPackage):
	"""Ensemble Taxonomic Assignments of Amplicon Sequencing Data

	Creates ensemble taxonomic assignments of amplicon sequencing data 
  in R using outputs of multiple taxonomic assignment algorithms and/or
	reference databases. Includes flexible algorithms for mapping taxonomic 
	nomenclatures onto one another and for computing ensemble taxonomic 
	assignments. 
	"""
	
	cran = "ensembleTax" 

	version("1.1.1", md5="9ccb3175daf323d8cee8b638f16fbe32")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-decipher", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-usethis", type=("build", "run"))
