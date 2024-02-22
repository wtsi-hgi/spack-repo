# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMutationtypes(RPackage):
	"""Validate and Convert Mutational Impacts Using Standard Genomic
Dictionaries

	Check concordance of a vector of mutation impacts with standard dictionaries such as Sequence Ontology (SO) <http://www.sequenceontology.org/>, Mutation Annotation Format (MAF) <https://docs.gdc.cancer.gov/Encyclopedia/pages/Mutation_Annotation_Format_TCGAv2/> or Prediction and Annotation of Variant Effects (PAVE) <https://github.com/hartwigmedical/hmftools/tree/master/pave>. 
  It enables conversion between SO/PAVE and MAF terms and selection of the most severe consequence where multiple ampersand (&) delimited impacts are given.
	"""
	
	homepage = "https://github.com/selkamand/mutationtypes"
	cran = "mutationtypes" 

	version("0.0.1", md5="d5d3af6c83922958b85921fef0cd3c5b")

	depends_on("r-assertions", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
