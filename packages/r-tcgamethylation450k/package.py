# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTcgamethylation450k(RPackage):
	"""The Cancer Genome Atlas Illumina 450k methylation example data

	The Cancer Genome Atlas (TCGA) is applying genomics technologies to over 20 different types of cancer.  This package contains a small set of 450k array data in idat format.
	"""
	
	bioc = "TCGAMethylation450k" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/TCGAMethylation450k_1.38.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/TCGAMethylation450k/TCGAMethylation450k_1.38.0.tar.gz"]

	version("1.38.0", md5="e913aa3b85d5cd1d0b27a346daf8c9ee")


	# experiment