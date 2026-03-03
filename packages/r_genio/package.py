# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenio(RPackage):
	"""Genetics Input/Output Functions

	Implements readers and writers for file formats associated with genetics data.  Reading and writing Plink BED/BIM/FAM and GCTA binary GRM formats is fully supported, including a lightning-fast BED reader and writer implementations.  Other functions are 'readr' wrappers that are more constrained, user-friendly, and efficient for these particular applications; handles Plink and Eigenstrat tables (FAM, BIM, IND, and SNP files).  There are also make functions for FAM and BIM tables with default values to go with simulated genotype data.
	"""
	
	homepage = "https://github.com/OchoaLab/genio"
	cran = "genio" 

	version("1.1.2", md5="e571367e715093bae50df70fe3abe99d")

	depends_on("r-readr@2:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
