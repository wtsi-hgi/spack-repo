# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSnvlfdr(RPackage):
	"""Empirical Bayes Single Nucleotide Variant Calling

	Identifies single nucleotide variants in next-generation sequencing data by estimating their local false discovery rates. For more details, see Karimnezhad, A. and Perkins, T. J. (2024) <doi:10.1038/s41598-024-51958-z>.
	"""
	
	cran = "SNVLFDR" 

	version("1.0.1", md5="92ca019e38ecf9e446ebe9835ad955d9")

