# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDfp(RPackage):
	"""Gene Selection

	This package provides a supervised technique able to identify differentially expressed genes, based on the construction of emph{Fuzzy Patterns} (FPs). The Fuzzy Patterns are built by means of applying 3 Membership Functions to discretized gene expression values.
	"""
	
	bioc = "DFP" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/DFP_1.60.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/DFP/DFP_1.60.0.tar.gz"]

	version("1.60.0", md5="5eb14fe67a6dd0599cd24c3473eec349")

	depends_on("r-biobase@2.5.5:", type=("build", "run"))
