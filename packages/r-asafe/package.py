# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAsafe(RPackage):
	"""Ancestry Specific Allele Frequency Estimation

	Given admixed individuals' bi-allelic SNP genotypes and ancestry pairs (where each ancestry can take one of three values) for multiple SNPs, perform an EM algorithm to deal with the fact that SNP genotypes are unphased with respect to ancestry pairs, in order to estimate ancestry-specific allele frequencies for all SNPs.
	"""
	
	bioc = "ASAFE" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ASAFE_1.28.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ASAFE/ASAFE_1.28.0.tar.gz"]

	version("1.28.0", md5="e054d986c3b6f2574c26498eaf6e4f7c")

	depends_on("r@3.2:", type=("build", "run"))
