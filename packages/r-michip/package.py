# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMichip(RPackage):
	"""MiChip Parsing and Summarizing Functions

	This package takes the MiChip miRNA microarray .grp scanner output files and parses these out, providing summary and plotting functions to analyse MiChip hybridizations. A set of hybridizations is packaged into an ExpressionSet allowing it to be used by other BioConductor packages.
	"""
	
	bioc = "MiChip" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/MiChip_1.56.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/MiChip/MiChip_1.56.0.tar.gz"]

	version("1.56.0", sha256="5697123140850b6fc6f2e5a1e6276c1b3c86409ca6977afa5eeacab7dc61e545")

	depends_on("r@2.3:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
