# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimtrait(RPackage):
	"""Simulate Complex Traits from Genotypes

	Simulate complex traits given a SNP genotype matrix and model parameters (the desired heritability, number of causal loci, and either the true ancestral allele frequencies used to generate the genotypes or the mean kinship for a real dataset).  Emphasis on avoiding common biases due to the use of estimated allele frequencies.  The code selects random loci to be causal, constructs coefficients for these loci and random independent non-genetic effects, and can optionally generate random group effects.  Traits can follow three models: random coefficients, fixed effect sizes, and infinitesimal (multivariate normal).  GWAS method benchmarking functions are also provided.  Described in Yao and Ochoa (2022) <doi:10.1101/2022.03.25.485885>.
	"""
	
	homepage = "https://github.com/OchoaLab/simtrait"
	cran = "simtrait" 

	version("1.1.3", md5="e6cd5ef7031e29e65a3add8bdd237d83")

	depends_on("r-prroc", type=("build", "run"))
