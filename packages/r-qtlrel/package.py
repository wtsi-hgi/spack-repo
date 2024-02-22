# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQtlrel(RPackage):
	"""Tools for Mapping of Quantitative Traits of Genetically Related
Individuals and Calculating Identity Coefficients from
Pedigrees

	This software provides tools for quantitative trait mapping in populations such as advanced intercross lines where relatedness among individuals should not be ignored. It can estimate background genetic variance components, impute missing genotypes, simulate genotypes, perform a genome scan for putative quantitative trait loci (QTL), and plot mapping results. It also has functions to calculate identity coefficients from pedigrees, especially suitable for pedigrees that consist of a large number of generations, or estimate identity coefficients from genotypic data in certain circumstances.
	"""
	
	cran = "QTLRel" 

	version("1.14", md5="7b11f45d9d2ad5b8de5ef5dadafbc38a")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-gdata", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
