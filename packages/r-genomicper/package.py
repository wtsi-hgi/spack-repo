# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenomicper(RPackage):
	"""Circular Genomic Permutation using Genome Wide Association
p-Values

	Circular genomic permutation approach uses genome wide association studies (GWAS) results to establish the significance of pathway/gene-set associations whilst accounting for genomic structure(Cabrera et al (2012) <doi:10.1534/g3.112.002618>). All single nucleotide polymorphisms (SNPs) in the GWAS are placed in a 'circular genome' according to their location. Then the complete set of SNP association p-values are permuted by rotation with respect to the SNPs' genomic locations. Two testing frameworks are available: permutations at the gene level, and permutations at the SNP level. The permutation at the gene level uses Fisher's combination test to calculate a single gene p-value, followed by the hypergeometric test. The SNP count methodology maps each SNP to pathways/gene-sets and calculates the proportion of SNPs for the real and the permutated datasets above a pre-defined threshold. Genomicper requires a matrix of GWAS association p-values and SNPs annotation to genes. Pathways can be obtained from within the package or can be provided by the user.
	"""
	
	cran = "genomicper" 

	version("1.7", md5="b41db09a5dbe1ccd1237da3b95f63195")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-reactome-db", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
