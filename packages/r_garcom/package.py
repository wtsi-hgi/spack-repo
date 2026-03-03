# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGarcom(RPackage):
	"""Gene and Region Counting of Mutations ("GARCOM")

	Gene and Region Counting of Mutations (GARCOM) package computes mutation (or alleles) counts per gene per individuals based on gene annotation or genomic base pair boundaries. It comes with features to accept data formats in plink(.raw) and VCF. It provides users flexibility to extract and filter individuals, mutations and genes of interest.
	"""
	
	cran = "GARCOM" 

	version("1.2.2", md5="daa6d56fdea5ae5a3f498406040bd40a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table@1.12.8:", type=("build", "run"))
	depends_on("r-vcfr@1.12:", type=("build", "run"))
