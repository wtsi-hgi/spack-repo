# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLdaandldas(RPackage):
	"""Linkage Disequilibrium of Ancestry (LDA) and LDA Score (LDAS)

	Computation of linkage disequilibrium of ancestry (LDA) and linkage disequilibrium of ancestry score (LDAS). LDA calculates the pairwise linkage disequilibrium of ancestry between single nucleotide polymorphisms (SNPs). LDAS calculates the LDA score of SNPs. The methods are described in Barrie W, Yang Y, Irving-Pease E.K, et al (2024) <doi:10.1038/s41586-023-06618-z>.
	"""
	
	cran = "LDAandLDAS" 

	version("1.1.3", md5="6b502545a8c5c9453b4b3ee44aa49da1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
