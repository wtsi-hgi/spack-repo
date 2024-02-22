# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimfam(RPackage):
	"""Simulate and Model Family Pedigrees with Structured Founders

	The focus is on simulating and modeling families with founders drawn from a structured population (for example, with different ancestries or other potentially non-family relatedness), in contrast to traditional pedigree analysis that treats all founders as equally unrelated.  Main function simulates a random pedigree for many generations, avoiding close relatives, pairing closest individuals according to a 1D geography and their randomly-drawn sex, and with variable children sizes to result in a target population size per generation.  Auxiliary functions calculate kinship matrices, admixture matrices, and draw random genotypes across arbitrary pedigree structures starting from the corresponding founder values.  The code is built around the plink FAM table format for pedigrees.  Described in Yao and Ochoa (2022) <doi:10.1101/2022.03.25.485885>.
	"""
	
	homepage = "https://github.com/OchoaLab/simfam"
	cran = "simfam" 

	version("1.1.6", md5="4dc4c483a4b257212445755cd641edae")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
