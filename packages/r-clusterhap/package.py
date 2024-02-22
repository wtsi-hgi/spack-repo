# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClusterhap(RPackage):
	"""Clustering Genotypes in Haplotypes

	One haplotype is a combination of SNP
  (Single Nucleotide Polymorphisms) within the QTL (Quantitative Trait Loci).
  clusterhap groups together all individuals of a population with the same haplotype.
  Each group contains individual with the same allele in each SNP,
  whether or not missing data. Thus, clusterhap groups individuals,
  that to be imputed, have a non-zero probability of having the same alleles
  in the entire sequence of SNP's. Moreover, clusterhap calculates such
  probability from relative frequencies.
	"""
	
	cran = "clusterhap" 

	version("0.1", md5="f35ae67a41572f6c3c866ed78ef5867d")

	depends_on("r@2.10:", type=("build", "run"))
