# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDgaselid(RPackage):
	"""Genetic Algorithm with Incomplete Dominance for Feature
Selection

	Feature selection from high dimensional data using a diploid
    genetic algorithm with Incomplete Dominance for genotype to phenotype mapping
    and Random Assortment of chromosomes approach to recombination.
	"""
	
	cran = "dGAselID" 

	version("1.2", md5="501ed9700562f9cc25e32536facc8fd1")

	depends_on("r@3.3.1:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-mlinterfaces", type=("build", "run"))
	depends_on("r-genefilter", type=("build", "run"))
	depends_on("r-all", type=("build", "run"))
