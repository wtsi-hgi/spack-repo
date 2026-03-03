# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCellorigins(RPackage):
	"""Finds RNASeq Source Tissues Using In Situ Hybridisation Data

	Finds the most likely originating tissue(s) and developmental stage(s) of tissue-specific RNA sequencing data. The package identifies both pure transcriptomes and mixtures of transcriptomes. The most likely identity is found through comparisons of the sequencing data with high-throughput in situ hybridisation patterns. Typical uses are the identification of cancer cell origins, validation of cell culture strain identities, validation of single-cell transcriptomes, and validation of identity and purity of flow-sorting and dissection sequencing products.
	"""
	
	cran = "cellOrigins" 

	version("0.1.3", md5="09c6a3859d3ec2fb32c91353936ec320")

	depends_on("r-iterpc", type=("build", "run"))
