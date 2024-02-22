# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REbgenotyping(RPackage):
	"""Genotyping and SNP Detection using Next Generation Sequencing
Data

	Genotyping the population using next generation sequencing data is essentially important for the rare variant detection. In order to distinguish the genomic structural variation from sequencing error, we propose a statistical model which involves the genotype effect through a latent variable to depict the distribution of non-reference allele frequency data among different samples and different genome loci, while decomposing the sequencing error into sample effect and positional effect. An ECM algorithm is implemented to estimate the model parameters, and then the genotypes and SNPs are inferred based on the empirical Bayes method.
	"""
	
	cran = "ebGenotyping" 

	version("2.0.1", md5="34dd8d258fe4e52937d9e46e9137415f")

