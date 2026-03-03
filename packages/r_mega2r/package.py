# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMega2r(RPackage):
	"""Accessing and Processing a 'Mega2' Genetic Database

	Uses as input genetic data that have been reformatted and
     stored in a 'SQLite' database; this database is initially created
     by the standalone 'mega2' C++ program (available freely from
     <https://watson.hgen.pitt.edu/register/>). Loads and manipulates
     data frames containing genotype, phenotype, and family
     information from the input 'SQLite' database, and decompresses
     needed subsets of the genotype data, on the fly, in a memory
     efficient manner.  We have also created several more functions
     that illustrate how to use the data frames as well as perform
     useful tasks: these permit one to run the 'pedgene' package to
     carry out gene-based association tests on family data using
     selected marker subsets, to run the 'SKAT' package to carry out
     gene-based association tests using selected marker subsets, to
     run the 'famSKATRC' package to carry out gene-based association
     tests on families (optionally) and with rare or common variants
     using selected marker subsets, to output the 'Mega2R' data as a
     VCF file and related files (for phenotype and family data), and
     to convert the data frames into CoreArray Genomic Data Structure
     (GDS) format.
	"""
	
	homepage = "https://watson.hgen.pitt.edu/mega2/mega2r/"
	cran = "Mega2R" 

	version("1.1.0", md5="14bb259cef74dd314fe1d25e9d7d36a7")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-skat", type=("build", "run"))
	depends_on("r-pedgene", type=("build", "run"))
	depends_on("r-gdsfmt", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-famskatrc", type=("build", "run"))
	depends_on("r-kinship2", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
