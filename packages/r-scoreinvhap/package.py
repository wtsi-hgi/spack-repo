# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScoreinvhap(RPackage):
	"""Get inversion status in predefined regions

	scoreInvHap can get the samples' inversion status of known inversions. scoreInvHap uses SNP data as input and requires the following information about the inversion: genotype frequencies in the different haplotypes, R2 between the region SNPs and inversion status and heterozygote genotypes in the reference. The package include this data for 21 inversions.
	"""
	
	bioc = "scoreInvHap"

	version("1.30.0", commit="6877ed19c1b2435ea3690ba96d5f80fb34f05fda")
	version("1.24.0", commit="644e352b1b0670b0861ea5238d5bde9f0ed6f519")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-snpstats", type=("build", "run"))
	depends_on("r-variantannotation", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
