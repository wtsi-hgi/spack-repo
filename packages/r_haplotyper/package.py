# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHaplotyper(RPackage):
	"""Tool for Clustering Genotypes in Haplotypes

	Function to  identify  haplotypes
  within QTL (Quantitative Trait Loci). One haplotype is a combination of SNP
  (Single Nucleotide Polymorphisms) within the QTL. This function groups
  together all individuals of a population with the same haplotype.
  Each group contains individual with the same allele in each SNP,
  whether or not missing data. Thus, haplotyper groups individuals,
  that to be imputed, have a non-zero probability of having the same alleles
  in the entire sequence of SNP's. Moreover, haplotyper calculates such
  probability from relative frequencies.
	"""
	
	cran = "haplotyper" 

	version("0.1", md5="2ffc9dfd94d7e1167e98f0b60036be34")

	depends_on("r@2.10:", type=("build", "run"))
