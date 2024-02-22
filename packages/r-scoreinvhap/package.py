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
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/scoreInvHap_1.24.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/scoreInvHap/scoreInvHap_1.24.0.tar.gz"]

	version("1.24.0", md5="7505f8161571dcc7b9b752fc62dedce5")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-snpstats", type=("build", "run"))
	depends_on("r-variantannotation", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
