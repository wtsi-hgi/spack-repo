# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLea(RPackage):
	"""LEA: an R package for Landscape and Ecological Association Studies

	LEA is an R package dedicated to population genomics, landscape genomics and genotype-environment association tests. LEA can run analyses of population structure and genome-wide tests for local adaptation, and also performs imputation of missing genotypes. The package includes statistical methods for estimating ancestry coefficients from large genotypic matrices and for evaluating the number of ancestral populations (snmf). It performs statistical tests using latent factor mixed models for identifying genetic polymorphisms that exhibit association with environmental gradients or phenotypic traits (lfmm2). In addition, LEA computes values of genetic offset statistics based on new or predicted environments (genetic.gap, genetic.offset). LEA is mainly based on optimized programs that can scale with the dimensions of large data sets.
	"""
	
	homepage = "http://membres-timc.imag.fr/Olivier.Francois/lea.html"
	bioc = "LEA"

	version("3.20.0", commit="4a4f03640c97f92b58d79d6d68ca7f4d80621ab6")
	version("3.14.0", commit="1765faca802583da16c69ba831ae8544076b8cfc")

	depends_on("r@3.3:", type=("build", "run"))
