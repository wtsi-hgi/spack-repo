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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/LEA_3.14.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/LEA/LEA_3.14.0.tar.gz"]

	version("3.14.0", md5="e32cbc2a97921f9b911eef1a5d1ef3d7")

	depends_on("r@3.3:", type=("build", "run"))
