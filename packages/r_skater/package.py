# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSkater(RPackage):
	"""Utilities for SNP-Based Kinship Analysis

	Utilities for single nucleotide polymorphism (SNP) based kinship analysis
    testing and evaluation. The 'skater' package contains functions for importing, parsing, 
    and analyzing pedigree data, performing relationship degree inference, benchmarking 
    relationship degree classification, and summarizing identity by descent (IBD) segment data.
    Package functions and methods are described in Turner et al. (2021) "skater: An R package 
    for SNP-based Kinship Analysis, Testing, and Evaluation" <doi:10.1101/2021.07.21.453083>.
	"""
	
	homepage = "https://github.com/signaturescience/skater"
	cran = "skater" 

	version("0.1.2", md5="abb954fe085c5817101ef2cd278f94b1")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-kinship2", type=("build", "run"))
	depends_on("r-corrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
