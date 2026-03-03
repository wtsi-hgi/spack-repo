# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKris(RPackage):
	"""Keen and Reliable Interface Subroutines for Bioinformatic
Analysis

	Provides useful functions which are needed for bioinformatic analysis such as calculating linear principal components from numeric data and Single-nucleotide polymorphism (SNP) dataset, calculating fixation index (Fst) using Hudson method, creating scatter plots in 3 views, handling with PLINK binary file format, detecting rough structures and outliers using unsupervised clustering, and calculating matrix multiplication in the faster way for big data.
	"""
	
	homepage = "https://gitlab.com/kris.ccp/kris"
	cran = "KRIS" 

	version("1.1.6", md5="4213e83cf6954b63cd51205d237f1783")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rarpack", type=("build", "run"))
