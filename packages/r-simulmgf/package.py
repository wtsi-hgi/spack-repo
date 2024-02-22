# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimulmgf(RPackage):
	"""Simulate SNP Matrix, Phenotype and Genotypic Effects

	Simulate genotypes in SNP (single nucleotide polymorphisms) Matrix as random numbers from an uniform distribution, for diploid organisms (coded by 0, 1, 2), Sikorska et al., (2013) <doi:10.1186/1471-2105-14-166>, or half-sib/full-sib SNP matrix from real or simulated parents SNP data, assuming mendelian segregation. Simulate phenotypic traits for real or simulated SNP data, controlled by a specific number of quantitative trait loci  and their effects, sampled from a Normal or an Uniform distributions, assuming a pure additive model. This is useful for testing association and genomic prediction models or for educational purposes.
	"""
	
	homepage = "https://github.com/mngar/simulMGF"
	cran = "simulMGF" 

	version("0.1.1", md5="45fd9577f03d055ccc7b3dd2a60bf4c1")

