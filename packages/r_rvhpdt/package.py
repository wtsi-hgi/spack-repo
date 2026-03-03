# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRvhpdt(RPackage):
	"""Calling Haplotype-Based and Variant-Based Pedigree
Disequilibrium Test for Rare Variants in Pedigrees

	To detecting rare variants for binary traits using general pedigrees, the pedigree disequilibrium tests are proposed by collapsing rare haplotypes/variants with/without weights. To run the test, MERLIN is needed in Linux for haplotyping.
	"""
	
	cran = "rvHPDT" 

	version("4.0", md5="e1b070a052627e5c07e98696898296ea")

	depends_on("r-gtools", type=("build", "run"))
	depends_on("r@2.15:", type=("build", "run"))
