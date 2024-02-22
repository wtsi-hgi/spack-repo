# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBedmatrix(RPackage):
	"""Extract Genotypes from a PLINK .bed File

	A matrix-like data structure that allows for efficient,
    convenient, and scalable subsetting of binary genotype/phenotype files
    generated by PLINK (<https://www.cog-genomics.org/plink2>), the whole
    genome association analysis toolset, without loading the entire file into
    memory.
	"""
	
	homepage = "https://github.com/QuantGen/BEDMatrix"
	cran = "BEDMatrix" 

	version("2.0.3", md5="edb1c568956bcbd9815022d0414b2124")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-crochet@2.3:", type=("build", "run"))
