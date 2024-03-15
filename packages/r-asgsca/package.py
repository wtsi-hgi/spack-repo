# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAsgsca(RPackage):
	"""Association Studies for multiple SNPs and multiple traits using Generalized Structured Equation Models

	The package provides tools to model and test the association between multiple genotypes and multiple traits, taking into account the prior biological knowledge. Genes, and clinical pathways are incorporated in the model as latent variables. The method is based on Generalized Structured Component Analysis (GSCA).
	"""
	
	bioc = "ASGSCA" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ASGSCA_1.36.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ASGSCA/ASGSCA_1.36.0.tar.gz"]

	version("1.36.0", md5="c0e60b4fa228444ab7863044881fa8bb")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
