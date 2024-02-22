# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlinkfile(RPackage):
	"""'PLINK' (and 'GCTA') File Helpers

	Reads/write binary genotype file compatible with 'PLINK' <https://www.cog-genomics.org/plink/1.9/input#bed> into/from a R matrix; traverse genotype data one windows of variants at a time, like apply() or a for loop; reads/writes genotype relatedness/kinship matrices created by 'PLINK' <https://www.cog-genomics.org/plink/1.9/distance#make_rel> or 'GCTA' <https://cnsgenomics.com/software/gcta/#MakingaGRM> into/from a R square matrix. It is best used for bringing data produced by 'PLINK' and 'GCTA' into R workflow.
	"""
	
	cran = "plinkFile" 

	version("0.2.1", md5="4061b459059cb51ad8f5f7a4f9f84ab6")

	depends_on("r@3.5:", type=("build", "run"))
