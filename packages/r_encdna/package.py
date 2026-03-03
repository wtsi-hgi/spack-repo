# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REncdna(RPackage):
	"""Encoding of Nucleotide Sequences into Numeric Feature Vectors

	We describe fifteen different splice site sequence encoding schemes that have been used in earlier studies for mapping of splice site sequences into numeric feature vectors. These encoding schemes will also be helpful for transforming other nucleotide sequences into numeric forms, provided they are of equal length. These encoding schemes will help the computational biologist working in the field of classification (binary or multiclass) or prediction involving nucleic acid sequences of equal length.
	"""
	
	cran = "EncDNA" 

	version("1.0.2", md5="48d5b2d867c00bc25dccfc1bdc4a96e3")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
